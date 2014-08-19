from PyQt4.QtGui import *
from PyQt4.QtCore import Qt, pyqtSlot, QThread, SIGNAL
from psim.gui.ui_main_window import *
import sys
from psim.gui.dtreewidget import DTreeWidget
from psim.gui.qtreeset import TreeSetQ, TreeQ
from psim.gui.dtypedialog import DTypeDialog
from psim.core.tree import EditHistory
import xml.etree.cElementTree as ET
import os.path

THIS=os.path.dirname(os.path.abspath(__file__))

class State(object):

    def __init__(self,tree):
        self.tree=TreeQ()
        self.tree.eh=EditHistory(ET.Element("edithistory"))
        self.tree.treeset=tree.treeset
        tokens=tree.tokens[:]
        for tidx,t in enumerate(tokens):
            t.index=tidx
        self.queue=tokens[:3]
        self.queue_rest=tokens[3:] #The invisible part of the queue
        self.stack=[]
        self.tree.tokens.extend(self.queue)
        self.transition_history=[]


    def done(self):
        return len(self.queue)==0 and len(self.stack)==1

    def undo(self):
        if len(self.transition_history)==0:
            return
        t,dtype,gov,dep=self.transition_history[-1]
        if t=="LA" or t=="RA":
            self.tree.editDepChange([(gov,dep,dtype,None,None,None)])
            if t=="LA":
                self.stack.insert(-1,self.tree.tokens[dep])
            elif t=="RA":
                self.stack.append(self.tree.tokens[dep])
            self.tree.hasChanged("generic")
        elif t=="SHIFT":
            self.queue.insert(0,self.stack.pop(-1))
        elif t=="SWAP":
            self.stack.insert(-1,self.queue.pop(0))
        self.transition_history.pop(-1)
        self.tree.eh.undo()

    def apply(self,action,dtype=None):
        if action=="SHIFT" and len(self.queue)>0:
            self.stack.append(self.queue.pop(0))
            self.transition_history.append((action,dtype,None,None))
            self.tree.eh.transition((action,dtype))
            if len(self.queue_rest)>0:
                self.tree.tokens.append(self.queue_rest[0])
                self.queue.append(self.queue_rest.pop(0))
                self.tree.hasChanged("generic")
        elif action=="LA" and len(self.stack)>=2 and dtype!=None:
            self.tree.editDepChange([(None,None,None,self.stack[-1].index,self.stack[-2].index,dtype)])
            self.transition_history.append((action,dtype,self.stack[-1].index,self.stack[-2].index))
            self.stack.pop(-2)
            self.tree.eh.transition((action,dtype))
            self.tree.hasChanged("generic")
        elif action=="RA" and len(self.stack)>=2 and dtype!=None:
            self.tree.editDepChange([(None,None,None,self.stack[-2].index,self.stack[-1].index,dtype)])
            self.transition_history.append((action,dtype,self.stack[-2].index,self.stack[-1].index))
            self.stack.pop(-1)
            self.tree.eh.transition((action,dtype))
            self.tree.hasChanged("generic")
        elif action=="SWAP" and len(self.stack)>1:
            self.queue.insert(0,self.stack.pop(-2))
            self.transition_history.append((action,dtype,None,None))
            self.tree.eh.transition((action,dtype))
        else: #Doesn't apply
            return

class Sim(QMainWindow):
    
    def __init__(self):
        QMainWindow.__init__(self)
        self.gui=Ui_MainWindow()
        self.gui.setupUi(self)
        self.connect(self.gui.LA,SIGNAL('clicked()'),self.LA)
        self.connect(self.gui.RA,SIGNAL('clicked()'),self.RA)
        self.connect(self.gui.SHIFT,SIGNAL('clicked()'),self.SHIFT)
        self.connect(self.gui.SWAP,SIGNAL('clicked()'),self.SWAP)
        self.connect(self.gui.undo,SIGNAL('clicked()'),self.undo)
        self.connect(self.gui.next,SIGNAL('clicked()'),self.next_sentence)
        self.gui.actionOpen.triggered.connect(self.open)

        self.curr_sent_idx=0
        self.w=DTreeWidget(self.gui.treeframe,readOnly=True)
        self.gui.treeframe.layout().addWidget(self.w)

    def update_view(self):
        self.gui.queue.setText(u" ".join(t.text for t in self.state.queue[:3]))
        self.gui.stack.setText(u" ".join(t.text for t in self.state.stack[-2:]))
        if len(self.state.transition_history)>0:
            self.gui.previoustransition.setText(u"Prev. transition: "+unicode(self.state.transition_history[-1]))
        else:
            self.gui.previoustransition.setText(u"Prev. transition: ---")

    def ask_type(self):
        x=DTypeDialog(self,os.path.join(THIS,"depTypes.txt"),"???")
        x.exec_()
        return x.selected #None if the user cancels

    def save(self):
        self.tset.save()

    @pyqtSlot()
    def next_sentence(self):
        if self.state.done() and self.curr_sent_idx<len(self.tset.sentences)-1:
            self.curr_sent_idx+=1
            self.set_sentence()

    def set_sentence(self):
        t=self.tset.sentences[self.curr_sent_idx]
        t.deps={}
        self.state=State(t)
        self.w.setModel(self.state.tree)
        self.update_view()

    @pyqtSlot()
    def open(self):
        fName=str(QFileDialog.getOpenFileName(self,"Open new .d.xml file","."))
        if not fName:
            return
        self.tset=TreeSetQ.fromFile(fName)
        self.curr_sent_idx=0
        self.set_sentence()

    @pyqtSlot()
    def save(self):
        print "Save"

    @pyqtSlot()
    def undo(self):
        self.state.undo()
        self.update_view()

    @pyqtSlot()
    def LA(self):
        if len(self.state.stack)<2:
            return
        self.state.apply("LA",self.ask_type())
        self.update_view()

    @pyqtSlot()
    def RA(self):
        if len(self.state.stack)<2:
            return
        self.state.apply("RA",self.ask_type())
        self.update_view()

    @pyqtSlot()
    def SHIFT(self):
        if len(self.state.queue)<1:
            return
        self.state.apply("SHIFT")
        self.update_view()

    @pyqtSlot()
    def SWAP(self):
        if len(self.state.stack)<2:
            return
        self.state.apply("SWAP")
        self.update_view()

def main(app):
    main_window=Sim()
    main_window.show()
    return app.exec_()    


if __name__=="__main__":
    app = QApplication(sys.argv)
    sys.exit(main(app))

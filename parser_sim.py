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

    def apply(self,action,dtype=None):
        if action=="SHIFT" and len(self.queue)>0:
            self.stack.append(self.queue.pop(0))
            if len(self.queue_rest)>0:
                self.tree.tokens.append(self.queue_rest[0])
                self.queue.append(self.queue_rest.pop(0))
                self.tree.hasChanged("generic")
        elif action=="LA" and len(self.stack)>=2 and dtype!=None:
            self.tree.editDepChange([(None,None,None,self.stack[-1].index,self.stack[-2].index,dtype)])
            self.stack.pop(-2)
            self.tree.hasChanged("generic")
        elif action=="RA" and len(self.stack)>=2 and dtype!=None:
            self.tree.editDepChange([(None,None,None,self.stack[-2].index,self.stack[-1].index,dtype)])
            self.stack.pop(-1)
            self.tree.hasChanged("generic")
        elif action=="SWAP" and len(self.stack)>0:
            self.queue.insert(0,self.stack.pop(-1))
            

class Sim(QMainWindow):
    
    def __init__(self):
        QMainWindow.__init__(self)
        self.gui=Ui_MainWindow()
        self.gui.setupUi(self)
        self.connect(self.gui.LA,SIGNAL('clicked()'),self.LA)
        self.connect(self.gui.RA,SIGNAL('clicked()'),self.RA)
        self.connect(self.gui.SHIFT,SIGNAL('clicked()'),self.SHIFT)
        self.connect(self.gui.SWAP,SIGNAL('clicked()'),self.SWAP)

        self.test()
        self.update_view()

    def update_view(self):
        self.gui.queue.setText(u" ".join(t.text for t in self.state.queue[:3]))
        self.gui.stack.setText(u" ".join(t.text for t in self.state.stack[-2:]))

    def ask_type(self):
        x=DTypeDialog(self,os.path.join(THIS,"depTypes.txt"),"???")
        x.exec_()
        return x.selected #None if the user cancels

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
        if len(self.state.stack)<1:
            return
        self.state.apply("SWAP")
        self.update_view()

    def test(self):
        tset=TreeSetQ.fromFile("b101-merged.d.xml")
        t=tset.sentences[1]
        t.deps={}
        w=DTreeWidget(self.gui.treeframe,readOnly=True)
        self.gui.treeframe.layout().addWidget(w)
        self.state=State(t)
        w.setModel(self.state.tree)

def main(app):
    main_window=Sim()
    main_window.show()
    return app.exec_()    


if __name__=="__main__":
    app = QApplication(sys.argv)
    sys.exit(main(app))

from PyQt4.QtGui import *
from PyQt4.QtCore import Qt, pyqtSlot, QThread, SIGNAL
from psim.gui.ui_main_window import *
import sys
from psim.gui.dtreewidget import DTreeWidget
from psim.gui.qtreeset import TreeSetQ
from psim.gui.dtypedialog import DTypeDialog
import os.path

THIS=os.path.dirname(os.path.abspath(__file__))

class State(object):

    def __init__(self,tree):
        self.tree=tree
        self.queue=[t.text for t in tree.tokens]
        self.stack=[]

    def apply(self,action,dtype=None):
        if action=="SHIFT" and len(self.queue)>0:
            self.stack.append(self.queue.pop(0))
        elif action=="LA" and len(self.stack)>=2 and dtype!=None:
            self.stack.pop(-2)
        elif action=="RA" and len(self.stack)>=2 and dtype!=None:
            self.stack.pop(-1)
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
        print self.state.queue
        self.gui.queue.setText(u" ".join(self.state.queue))
        self.gui.stack.setText(u" ".join(self.state.stack))

    def ask_type(self):
        x=DTypeDialog(self,os.path.join(THIS,"depTypes.txt"),"???")
        x.exec_()
        return x.selected #None if the user cancels

    @pyqtSlot()
    def LA(self):
        self.state.apply("LA",self.ask_type())
        self.update_view()

    @pyqtSlot()
    def RA(self):
        self.state.apply("RA",self.ask_type())
        self.update_view()

    @pyqtSlot()
    def SHIFT(self):
        self.state.apply("SHIFT")
        self.update_view()

    @pyqtSlot()
    def SWAP(self):
        self.state.apply("SWAP")
        self.update_view()

    def test(self):
        tset=TreeSetQ.fromFile("b101-merged.d.xml")
        t=tset.sentences[1]
        w=DTreeWidget(self.gui.treeframe,readOnly=True)
        w.setModel(t)
        self.state=State(t)

        
    

def main(app):
    main_window=Sim()
    main_window.show()
    return app.exec_()    


if __name__=="__main__":
    app = QApplication(sys.argv)
    sys.exit(main(app))

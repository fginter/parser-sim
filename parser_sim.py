from PyQt4.QtGui import *
from PyQt4.QtCore import Qt, pyqtSlot, QThread
from psim.gui.ui_main_window import *
import sys
from psim.gui.dtreewidget import DTreeWidget
from psim.gui.qtreeset import TreeSetQ


class Sim(QMainWindow):
    
    def __init__(self):
        QMainWindow.__init__(self)
        self.gui=Ui_MainWindow()
        self.gui.setupUi(self)
        self.test()

    def test(self):
        tset=TreeSetQ.fromFile("b101-merged.d.xml")
        t=tset.sentences[1]
        w=DTreeWidget(self.gui.treeframe,readOnly=True)
        w.setModel(t)
        
        

def main(app):
    main_window=Sim()
    main_window.show()
    return app.exec_()    


if __name__=="__main__":
    app = QApplication(sys.argv)
    sys.exit(main(app))

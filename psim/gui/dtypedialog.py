from PyQt4.QtCore import *
from PyQt4.QtGui import *

class TypeButton(QPushButton):

    def __init__(self,dType,parent):
        QPushButton.__init__(self,dType,parent)
        self.parent=parent
        self.dType=dType.replace("&","").lower()
        self.connect(self,SIGNAL("clicked()"),SLOT("clicked()"))

    
    @pyqtSignature("")
    def clicked(self):
        self.parent.selectType(self.dType)


    def keyPressEvent(self,e):
        e.ignore()


class DTypeDialog(QDialog):

    def __init__(self,parent,depTypesFile, title ,cols=5):
        QDialog.__init__(self,parent)

        self.mainLayout=QGridLayout(self)
        self.selected = None
        self.hotkeys = {}

        depTypes=open(depTypesFile, "r")

        row=0
        col=0
        for depType in depTypes:
            depType = depType.strip()
            if not depType:
                row+=1
                col=0
                self.mainLayout.setRowMinimumHeight(row,10)
                row+=1
                continue

            dotIdx=depType.find(".")
            if dotIdx>=0:
                hotkey=depType[dotIdx+1]
            else:
                hotkey=None

            button=TypeButton(depType.replace(".","&"), self)
            self.mainLayout.addWidget(button,row,col)

            if hotkey:
                self.hotkeys[hotkey]=depType.replace(".","").lower()

            col+=1
            if col==cols:
                col=0
                row+=1


        button=QPushButton("Cancel",self)
        self.mainLayout.addWidget(button,row+1,0,1,-1)
        self.connect(button,SIGNAL("clicked()"),SLOT("reject()"))
        
        self.setLayout(self.mainLayout)
        self.setWindowTitle(title)
        self.setModal(True)

        depTypes.close()
        
        
    @pyqtSignature("")
    def selectType(self, dType):
        """Called by one of the buttons"""
        self.selected=dType
        self.accept()


    def keyPressEvent(self,e):
        if e.key()==Qt.Key_Escape:
            self.reject() # Close DTypeDialog when pressing ESC

        k=str(e.text())
        if k in self.hotkeys:
            self.selectType(self.hotkeys[k])

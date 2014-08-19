# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main_window.ui'
#
# Created: Tue Aug 19 11:58:03 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 438)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.treeframe = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeframe.sizePolicy().hasHeightForWidth())
        self.treeframe.setSizePolicy(sizePolicy)
        self.treeframe.setFrameShape(QtGui.QFrame.StyledPanel)
        self.treeframe.setFrameShadow(QtGui.QFrame.Raised)
        self.treeframe.setObjectName(_fromUtf8("treeframe"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.treeframe)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_3 = QtGui.QLabel(self.treeframe)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.verticalLayout.addWidget(self.treeframe)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setVerticalSpacing(13)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.queue = QtGui.QLabel(self.centralwidget)
        self.queue.setFrameShape(QtGui.QFrame.Box)
        self.queue.setObjectName(_fromUtf8("queue"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.queue)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.stack = QtGui.QLabel(self.centralwidget)
        self.stack.setFrameShape(QtGui.QFrame.Box)
        self.stack.setObjectName(_fromUtf8("stack"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.stack)
        self.verticalLayout.addLayout(self.formLayout)
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.LA = QtGui.QPushButton(self.frame)
        self.LA.setObjectName(_fromUtf8("LA"))
        self.horizontalLayout.addWidget(self.LA)
        self.RA = QtGui.QPushButton(self.frame)
        self.RA.setObjectName(_fromUtf8("RA"))
        self.horizontalLayout.addWidget(self.RA)
        self.SHIFT = QtGui.QPushButton(self.frame)
        self.SHIFT.setObjectName(_fromUtf8("SHIFT"))
        self.horizontalLayout.addWidget(self.SHIFT)
        self.SWAP = QtGui.QPushButton(self.frame)
        self.SWAP.setObjectName(_fromUtf8("SWAP"))
        self.horizontalLayout.addWidget(self.SWAP)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_3.setText(_translate("MainWindow", "TextLabel", None))
        self.label.setText(_translate("MainWindow", "Queue", None))
        self.queue.setText(_translate("MainWindow", "---", None))
        self.label_2.setText(_translate("MainWindow", "Stack", None))
        self.stack.setText(_translate("MainWindow", "---", None))
        self.LA.setText(_translate("MainWindow", "LEFT ARC", None))
        self.RA.setText(_translate("MainWindow", "RIGHT ARC", None))
        self.SHIFT.setText(_translate("MainWindow", "SHIFT", None))
        self.SWAP.setText(_translate("MainWindow", "SWAP", None))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'viewHelloWorld.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(713, 521)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lblMain = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(27)
        font.setBold(True)
        font.setWeight(75)
        self.lblMain.setFont(font)
        self.lblMain.setAlignment(QtCore.Qt.AlignCenter)
        self.lblMain.setObjectName("lblMain")
        self.verticalLayout_4.addWidget(self.lblMain)
        self.btnQuit = QtWidgets.QPushButton(Dialog)
        self.btnQuit.setObjectName("btnQuit")
        self.verticalLayout_4.addWidget(self.btnQuit)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_4.addWidget(self.pushButton)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lblMain.setText(_translate("Dialog", "Hello World"))
        self.btnQuit.setText(_translate("Dialog", "Quit"))
        self.pushButton.setText(_translate("Dialog", "PushButton"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


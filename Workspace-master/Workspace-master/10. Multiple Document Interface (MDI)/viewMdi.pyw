# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mdi.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(718, 551)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.mdiArea = QtWidgets.QMdiArea(Form)
        self.mdiArea.setObjectName("mdiArea")
        self.gridLayout.addWidget(self.mdiArea, 0, 0, 1, 3)
        self.btnNext = QtWidgets.QPushButton(Form)
        self.btnNext.setObjectName("btnNext")
        self.gridLayout.addWidget(self.btnNext, 1, 0, 1, 1)
        self.btnPrev = QtWidgets.QPushButton(Form)
        self.btnPrev.setObjectName("btnPrev")
        self.gridLayout.addWidget(self.btnPrev, 1, 1, 1, 1)
        self.btnCloseAll = QtWidgets.QPushButton(Form)
        self.btnCloseAll.setObjectName("btnCloseAll")
        self.gridLayout.addWidget(self.btnCloseAll, 1, 2, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnCascade = QtWidgets.QPushButton(Form)
        self.btnCascade.setObjectName("btnCascade")
        self.horizontalLayout.addWidget(self.btnCascade)
        self.btnTile = QtWidgets.QPushButton(Form)
        self.btnTile.setObjectName("btnTile")
        self.horizontalLayout.addWidget(self.btnTile)
        self.btnSubWinView = QtWidgets.QPushButton(Form)
        self.btnSubWinView.setObjectName("btnSubWinView")
        self.horizontalLayout.addWidget(self.btnSubWinView)
        self.btnTabView = QtWidgets.QPushButton(Form)
        self.btnTabView.setObjectName("btnTabView")
        self.horizontalLayout.addWidget(self.btnTabView)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btnNext.setText(_translate("Form", "Next"))
        self.btnPrev.setText(_translate("Form", "Prev"))
        self.btnCloseAll.setText(_translate("Form", "Close All"))
        self.btnCascade.setText(_translate("Form", "Cascade"))
        self.btnTile.setText(_translate("Form", "Tile"))
        self.btnSubWinView.setText(_translate("Form", "Subwindow View"))
        self.btnTabView.setText(_translate("Form", "Tabbed View"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


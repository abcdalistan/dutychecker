# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'viewListInput.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(598, 381)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.txtText = QtWidgets.QLineEdit(Form)
        self.txtText.setObjectName("txtText")
        self.gridLayout.addWidget(self.txtText, 0, 1, 1, 1)
        self.btnAdd = QtWidgets.QPushButton(Form)
        self.btnAdd.setObjectName("btnAdd")
        self.gridLayout.addWidget(self.btnAdd, 1, 0, 1, 1)
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 1, 1, 4, 1)
        self.btnEdit = QtWidgets.QPushButton(Form)
        self.btnEdit.setObjectName("btnEdit")
        self.gridLayout.addWidget(self.btnEdit, 2, 0, 1, 1)
        self.btnDelete = QtWidgets.QPushButton(Form)
        self.btnDelete.setObjectName("btnDelete")
        self.gridLayout.addWidget(self.btnDelete, 3, 0, 1, 1)
        self.btnDeleteAll = QtWidgets.QPushButton(Form)
        self.btnDeleteAll.setObjectName("btnDeleteAll")
        self.gridLayout.addWidget(self.btnDeleteAll, 4, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Text"))
        self.btnAdd.setText(_translate("Form", "Add"))
        self.btnEdit.setText(_translate("Form", "Edit"))
        self.btnDelete.setText(_translate("Form", "Delete"))
        self.btnDeleteAll.setText(_translate("Form", "Delete All"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


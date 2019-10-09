# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'viewRadChk.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 234)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radLarge = QtWidgets.QRadioButton(self.groupBox)
        self.radLarge.setObjectName("radLarge")
        self.verticalLayout.addWidget(self.radLarge)
        self.radMed = QtWidgets.QRadioButton(self.groupBox)
        self.radMed.setObjectName("radMed")
        self.verticalLayout.addWidget(self.radMed)
        self.radSmall = QtWidgets.QRadioButton(self.groupBox)
        self.radSmall.setObjectName("radSmall")
        self.verticalLayout.addWidget(self.radSmall)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 2, 1)
        self.lblTotal = QtWidgets.QLabel(Form)
        self.lblTotal.setObjectName("lblTotal")
        self.gridLayout.addWidget(self.lblTotal, 3, 0, 1, 1)
        self.chkChips = QtWidgets.QCheckBox(Form)
        self.chkChips.setObjectName("chkChips")
        self.gridLayout.addWidget(self.chkChips, 0, 1, 1, 1)
        self.chkCooldrink = QtWidgets.QCheckBox(Form)
        self.chkCooldrink.setObjectName("chkCooldrink")
        self.gridLayout.addWidget(self.chkCooldrink, 1, 1, 1, 1)
        self.spinbox = QtWidgets.QSpinBox(Form)
        self.spinbox.setObjectName("spinbox")
        self.gridLayout.addWidget(self.spinbox, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "Burgers"))
        self.radLarge.setText(_translate("Form", "Large $6"))
        self.radMed.setText(_translate("Form", "Med $5"))
        self.radSmall.setText(_translate("Form", "Small $4"))
        self.lblTotal.setText(_translate("Form", "TextLabel"))
        self.chkChips.setText(_translate("Form", "Chips $4"))
        self.chkCooldrink.setText(_translate("Form", "CoolDrink $5"))
        self.label_2.setText(_translate("Form", "Nr of Customer/Orders"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


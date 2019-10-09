# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'viewDateCalendarCombo.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(723, 465)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.cmbClass = QtWidgets.QComboBox(Form)
        self.cmbClass.setObjectName("cmbClass")
        self.gridLayout.addWidget(self.cmbClass, 3, 1, 1, 1)
        self.calendarWidget = QtWidgets.QCalendarWidget(Form)
        self.calendarWidget.setObjectName("calendarWidget")
        self.gridLayout.addWidget(self.calendarWidget, 1, 1, 1, 1)
        self.spnPersons = QtWidgets.QSpinBox(Form)
        self.spnPersons.setObjectName("spnPersons")
        self.gridLayout.addWidget(self.spnPersons, 2, 1, 1, 1)
        self.btnCalc = QtWidgets.QPushButton(Form)
        self.btnCalc.setObjectName("btnCalc")
        self.gridLayout.addWidget(self.btnCalc, 4, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.lblSummery = QtWidgets.QLabel(Form)
        self.lblSummery.setObjectName("lblSummery")
        self.gridLayout.addWidget(self.lblSummery, 5, 0, 1, 2)
        self.lblCost = QtWidgets.QLabel(Form)
        self.lblCost.setObjectName("lblCost")
        self.gridLayout.addWidget(self.lblCost, 6, 0, 1, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "Persons"))
        self.label_4.setText(_translate("Form", "Ticket Class"))
        self.btnCalc.setText(_translate("Form", "Calculate"))
        self.label_2.setText(_translate("Form", "Reservation Date"))
        self.label.setText(_translate("Form", "Ticket Reservation"))
        self.lblSummery.setText(_translate("Form", "Sumery"))
        self.lblCost.setText(_translate("Form", "Cost"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


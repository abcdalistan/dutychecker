# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_addwindow(object):
    def setupUi(self, addwindow):
        addwindow.setObjectName("addwindow")
        addwindow.resize(329, 210)
        addwindow.setMinimumSize(QtCore.QSize(329, 210))
        addwindow.setMaximumSize(QtCore.QSize(329, 210))
        addwindow.setStyleSheet("background-color: rgb(39, 39, 39);")
        self.centralwidget = QtWidgets.QWidget(addwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 170, 75, 23))
        self.pushButton.setStyleSheet("background-color: rgb(226, 226, 226);")
        self.pushButton.setObjectName("pushButton")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 301, 31))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setStyleSheet("font: 14pt \"Bebas\";\n"
"color: rgb(255, 255, 0);")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.fnamebox = QtWidgets.QLineEdit(self.layoutWidget)
        self.fnamebox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.fnamebox.setObjectName("fnamebox")
        self.horizontalLayout.addWidget(self.fnamebox)
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 100, 301, 31))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_2.setStyleSheet("font: 14pt \"Bebas\";\n"
"color: rgb(255, 255, 0);")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.idbox = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.idbox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.idbox.setObjectName("idbox")
        self.horizontalLayout_2.addWidget(self.idbox)
        self.layoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_3.setGeometry(QtCore.QRect(10, 130, 301, 31))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_3.setStyleSheet("font: 14pt \"Bebas\";\n"
"color: rgb(255, 255, 0);")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.posbox = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.posbox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.posbox.setObjectName("posbox")
        self.horizontalLayout_3.addWidget(self.posbox)
        self.layoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_4.setGeometry(QtCore.QRect(10, 40, 301, 31))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_ = QtWidgets.QLabel(self.layoutWidget_4)
        self.label_.setStyleSheet("font: 14pt \"Bebas\";\n"
"color: rgb(255, 255, 0);")
        self.label_.setObjectName("label_")
        self.horizontalLayout_4.addWidget(self.label_)
        self.lnamebox = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.lnamebox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lnamebox.setObjectName("lnamebox")
        self.horizontalLayout_4.addWidget(self.lnamebox)
        self.layoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_5.setGeometry(QtCore.QRect(10, 70, 301, 31))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget_5)
        self.label_5.setStyleSheet("font: 14pt \"Bebas\";\n"
"color: rgb(255, 255, 0);")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.cbox = QtWidgets.QLineEdit(self.layoutWidget_5)
        self.cbox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cbox.setObjectName("cbox")
        self.horizontalLayout_5.addWidget(self.cbox)
        self.pushButton.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget_2.raise_()
        self.layoutWidget_3.raise_()
        self.layoutWidget_4.raise_()
        self.label_3.raise_()
        self.layoutWidget_5.raise_()
        addwindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(addwindow)
        self.statusbar.setObjectName("statusbar")
        addwindow.setStatusBar(self.statusbar)

        self.retranslateUi(addwindow)
        QtCore.QMetaObject.connectSlotsByName(addwindow)

    def retranslateUi(self, addwindow):
        _translate = QtCore.QCoreApplication.translate
        addwindow.setWindowTitle(_translate("addwindow", "MainWindow"))
        self.pushButton.setText(_translate("addwindow", "Confirm"))
        self.label.setText(_translate("addwindow", "first Name:"))
        self.label_2.setText(_translate("addwindow", "Student ID: "))
        self.label_3.setText(_translate("addwindow", "Position:          "))
        self.label_.setText(_translate("addwindow", "Last Name:  "))
        self.label_5.setText(_translate("addwindow", "Course:               "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    addwindow = QtWidgets.QMainWindow()
    ui = Ui_addwindow()
    ui.setupUi(addwindow)
    addwindow.show()
    sys.exit(app.exec_())

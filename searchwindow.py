# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'searchwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_updatewindow(object):
    def setupUi(self, updatewindow):
        updatewindow.setObjectName("updatewindow")
        updatewindow.resize(329, 210)
        updatewindow.setMinimumSize(QtCore.QSize(329, 210))
        updatewindow.setMaximumSize(QtCore.QSize(329, 210))
        updatewindow.setStyleSheet("background-color: rgb(39, 39, 39);")
        self.centralwidget = QtWidgets.QWidget(updatewindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 160, 75, 23))
        self.pushButton.setStyleSheet("background-color: rgb(226, 226, 226);")
        self.pushButton.setObjectName("pushButton")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 40, 311, 31))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.firstname = QtWidgets.QLabel(self.layoutWidget)
        self.firstname.setStyleSheet("font: 14pt \"Bebas\";\n"
"color: rgb(255, 255, 0);")
        self.firstname.setObjectName("firstname")
        self.horizontalLayout.addWidget(self.firstname)
        self.fnamebox = QtWidgets.QLineEdit(self.layoutWidget)
        self.fnamebox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.fnamebox.setObjectName("fnamebox")
        self.horizontalLayout.addWidget(self.fnamebox)
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 70, 311, 31))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.studentid = QtWidgets.QLabel(self.layoutWidget_2)
        self.studentid.setStyleSheet("font: 14pt \"Bebas\";\n"
"color: rgb(255, 255, 0);")
        self.studentid.setObjectName("studentid")
        self.horizontalLayout_2.addWidget(self.studentid)
        self.idbox = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.idbox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.idbox.setObjectName("idbox")
        self.horizontalLayout_2.addWidget(self.idbox)
        self.layoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_3.setGeometry(QtCore.QRect(10, 130, 311, 31))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.position = QtWidgets.QLabel(self.layoutWidget_3)
        self.position.setStyleSheet("font: 14pt \"Bebas\";\n"
"color: rgb(255, 255, 0);")
        self.position.setObjectName("position")
        self.horizontalLayout_3.addWidget(self.position)
        self.posbox = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.posbox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.posbox.setObjectName("posbox")
        self.horizontalLayout_3.addWidget(self.posbox)
        self.layoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_4.setGeometry(QtCore.QRect(10, 10, 311, 31))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lastname = QtWidgets.QLabel(self.layoutWidget_4)
        self.lastname.setStyleSheet("font: 14pt \"Bebas\";\n"
"color: rgb(255, 255, 0);")
        self.lastname.setObjectName("lastname")
        self.horizontalLayout_4.addWidget(self.lastname)
        self.lnamebox = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.lnamebox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lnamebox.setObjectName("lnamebox")
        self.horizontalLayout_4.addWidget(self.lnamebox)
        self.layoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_5.setGeometry(QtCore.QRect(10, 100, 311, 31))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.course = QtWidgets.QLabel(self.layoutWidget_5)
        self.course.setStyleSheet("font: 14pt \"Bebas\";\n"
"color: rgb(255, 255, 0);")
        self.course.setObjectName("course")
        self.horizontalLayout_5.addWidget(self.course)
        self.cbox = QtWidgets.QLineEdit(self.layoutWidget_5)
        self.cbox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cbox.setObjectName("cbox")
        self.horizontalLayout_5.addWidget(self.cbox)
        updatewindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(updatewindow)
        self.statusbar.setObjectName("statusbar")
        updatewindow.setStatusBar(self.statusbar)

        self.retranslateUi(updatewindow)
        QtCore.QMetaObject.connectSlotsByName(updatewindow)

    def retranslateUi(self, updatewindow):
        _translate = QtCore.QCoreApplication.translate
        updatewindow.setWindowTitle(_translate("updatewindow", "MainWindow"))
        self.pushButton.setText(_translate("updatewindow", "Confirm"))
        self.firstname.setText(_translate("updatewindow", "first Name:"))
        self.studentid.setText(_translate("updatewindow", "Student ID: "))
        self.position.setText(_translate("updatewindow", "Position:          "))
        self.lastname.setText(_translate("updatewindow", "Last Name:  "))
        self.course.setText(_translate("updatewindow", "Course:               "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    updatewindow = QtWidgets.QMainWindow()
    ui = Ui_updatewindow()
    ui.setupUi(updatewindow)
    updatewindow.show()
    sys.exit(app.exec_())

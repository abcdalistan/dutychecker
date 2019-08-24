# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'deletewindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_deletewindow(object):
    def setupUi(self, deletewindow):
        deletewindow.setObjectName("deletewindow")
        deletewindow.resize(345, 110)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(deletewindow.sizePolicy().hasHeightForWidth())
        deletewindow.setSizePolicy(sizePolicy)
        deletewindow.setMinimumSize(QtCore.QSize(345, 110))
        deletewindow.setMaximumSize(QtCore.QSize(345, 110))
        deletewindow.setStyleSheet("background-color: rgb(43, 43, 43);")
        self.centralwidget = QtWidgets.QWidget(deletewindow)
        self.centralwidget.setObjectName("centralwidget")
        self.delconfirm = QtWidgets.QPushButton(self.centralwidget)
        self.delconfirm.setGeometry(QtCore.QRect(130, 70, 75, 23))
        self.delconfirm.setStyleSheet("background-color: rgb(225, 225, 225);")
        self.delconfirm.setObjectName("delconfirm")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 20, 321, 41))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.delname = QtWidgets.QLabel(self.widget)
        self.delname.setStyleSheet("color: rgb(255, 255, 0);\n"
"font: 16pt \"Bebas\";")
        self.delname.setObjectName("delname")
        self.horizontalLayout.addWidget(self.delname)
        self.delnamebox = QtWidgets.QLineEdit(self.widget)
        self.delnamebox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.delnamebox.setObjectName("delnamebox")
        self.horizontalLayout.addWidget(self.delnamebox)
        deletewindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(deletewindow)
        self.statusbar.setObjectName("statusbar")
        deletewindow.setStatusBar(self.statusbar)

        self.retranslateUi(deletewindow)
        QtCore.QMetaObject.connectSlotsByName(deletewindow)

    def retranslateUi(self, deletewindow):
        _translate = QtCore.QCoreApplication.translate
        deletewindow.setWindowTitle(_translate("deletewindow", "MainWindow"))
        self.delconfirm.setText(_translate("deletewindow", "Confirm"))
        self.delname.setText(_translate("deletewindow", "Name:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    deletewindow = QtWidgets.QMainWindow()
    ui = Ui_deletewindow()
    ui.setupUi(deletewindow)
    deletewindow.show()
    sys.exit(app.exec_())

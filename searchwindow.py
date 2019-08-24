# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'searchwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_searchwindow(object):
    def setupUi(self, searchwindow):
        searchwindow.setObjectName("searchwindow")
        searchwindow.resize(345, 110)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(searchwindow.sizePolicy().hasHeightForWidth())
        searchwindow.setSizePolicy(sizePolicy)
        searchwindow.setMinimumSize(QtCore.QSize(345, 110))
        searchwindow.setMaximumSize(QtCore.QSize(345, 110))
        searchwindow.setStyleSheet("background-color: rgb(33, 33, 33);\n"
"font: 8pt \"MS Shell Dlg 2\";")
        self.centralwidget = QtWidgets.QWidget(searchwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.searchbut = QtWidgets.QPushButton(self.centralwidget)
        self.searchbut.setGeometry(QtCore.QRect(140, 70, 75, 23))
        self.searchbut.setStyleSheet("background-color: rgb(226, 226, 226);")
        self.searchbut.setObjectName("searchbut")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 321, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.sername = QtWidgets.QLabel(self.layoutWidget)
        self.sername.setStyleSheet("color: rgb(255, 255, 0);\n"
"font: 16pt \"Bebas\";")
        self.sername.setObjectName("sername")
        self.horizontalLayout.addWidget(self.sername)
        self.sernamebox = QtWidgets.QLineEdit(self.layoutWidget)
        self.sernamebox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.sernamebox.setObjectName("sernamebox")
        self.horizontalLayout.addWidget(self.sernamebox)
        searchwindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(searchwindow)
        self.statusbar.setObjectName("statusbar")
        searchwindow.setStatusBar(self.statusbar)

        self.retranslateUi(searchwindow)
        QtCore.QMetaObject.connectSlotsByName(searchwindow)

    def retranslateUi(self, searchwindow):
        _translate = QtCore.QCoreApplication.translate
        searchwindow.setWindowTitle(_translate("searchwindow", "MainWindow"))
        self.searchbut.setText(_translate("searchwindow", "Search"))
        self.sername.setText(_translate("searchwindow", "Name:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    searchwindow = QtWidgets.QMainWindow()
    ui = Ui_searchwindow()
    ui.setupUi(searchwindow)
    searchwindow.show()
    sys.exit(app.exec_())

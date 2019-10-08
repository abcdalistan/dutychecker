from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox
import pymysql
from PyQt5.QtCore import QCoreApplication,Qt,QBasicTimer,QPoint


class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(953, 627)
        MainWindow.setStyleSheet("background:transparent;")
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, -50, 1011, 701))
        self.label.setObjectName("label")

        self.ctable = QtWidgets.QTableWidget(self.centralwidget)
        self.ctable.setGeometry(QtCore.QRect(230, 80, 631, 441))
        self.ctable.setFrameShape(QtWidgets.QFrame.Box)
        self.ctable.setLineWidth(1)
        self.ctable.setObjectName("ctable")
        self.ctable.setColumnCount(6)
        self.ctable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.ctable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ctable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.ctable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.ctable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.ctable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.ctable.setHorizontalHeaderItem(5, item)
        self.ctable.horizontalHeader().setDefaultSectionSize(156)
        self.ctable.horizontalHeader().setMinimumSectionSize(156)
        self.ctable.horizontalHeader().setSortIndicatorShown(False)
        self.ctable.horizontalHeader().setStretchLastSection(False)
        self.ctable.setStyleSheet("Background:White")

        self.exitbut = QtWidgets.QPushButton(self.centralwidget)
        self.exitbut.setGeometry(QtCore.QRect(70, 90, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Nexa Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.exitbut.setFont(font)
        self.exitbut.setStyleSheet("QPushButton {background-color: Black} QPushButton:hover {background-color:grey}QPushButton {border-radius:15px}QPushButton {color:White}QPushButton{border:2px solid yellow}QPushButton:pressed{Background-color:red};")
        self.exitbut.setObjectName("exitbut")
        self.exitbut.clicked.connect(lambda closeFunction: MainWindow.close())

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/login/Pics/Admin-window.png\"width=850 height=500/></p></body></html>"))
        item = self.ctable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Student ID"))
        item = self.ctable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "First Name"))
        item = self.ctable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Last Name"))
        item = self.ctable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Program"))
        item = self.ctable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Date"))
        item = self.ctable.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Fine"))
        self.exitbut.setText(_translate("MainWindow", "Exit"))
import dutycheckerFiles_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

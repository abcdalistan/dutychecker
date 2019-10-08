from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import pymysql
from PyQt5.QtCore import QCoreApplication,Qt,QBasicTimer,QPoint
from Newdutysched import Ui_MainWindow

class Ui_viewwindow(QMainWindow):
    # def cell_was_clicked(self, row, column):
    #     self.row = row
    #     return None

    # def addTable(self,columns):
    #     rowPosition=self.ctable.rowCount()
    #     self.ctable.insertRow(rowPosition)
    #     for i, column in enumerate(columns):
    #         self.ctable.setItem(rowPosition,i, QtWidgets.QTableWidgetItem(str(column)))
    #     return None

    # def viewStaffer(self):
    #     if self.flag:
    #         conn = pymysql.connect('localhost', 'root', '', 'staffer')
    #         with conn:
    #             cur = conn.cursor()
    #             query = ("SELECT ls.login_time, ls.logout_time, si.first_name, ls.status, ls.date FROM loginstaff ls INNER JOIN stafferinfo si on ls.student_number=si.student_number")
    #             cur.execute(query)
    #             staffers = cur.fetchall()
    #             print(staffers)
    #             for row in staffers:
    #                 self.addTable(row)
    #             cur.close()
    #         self.flag = 0
    #     return None

    # def refreshfunc(self):
    #     self.ctable.setRowCount(0)
    #     conn = pymysql.connect('localhost', 'root', '', 'staffer')
    #     with conn:
    #         cur=conn.cursor()
    #         query=("SELECT ls.login_time, ls.logout_time, si.first_name, ls.status, ls.date FROM loginstaff ls INNER JOIN stafferinfo si on ls.student_number=si.student_number WHERE ls.status = 0")
    #         cur.execute(query)
    #         result = cur.fetchall()
    #         for row in result:
    #             self.addTable(row)
    #             cur.close()
    #     return None
    
    #   NOT IN

    def cell_was_clicked(self, row, column):
        self.row = row
        return None

    def addTable(self,columns):
        rowPosition=self.ctable.rowCount()
        self.ctable.insertRow(rowPosition)
        for i, column in enumerate(columns):
            self.ctable.setItem(rowPosition,i, QtWidgets.QTableWidgetItem(str(column)))
        return None

    def viewStaffer(self):
        if self.flag:
            conn = pymysql.connect('localhost', 'tipvoice', 'password', 'staffer')
            with conn:
                cur = conn.cursor()
                query = """SELECT ls.login_time, ls.logout_time, si.first_name, ls.status, ls.date FROM loginstaff ls 
                INNER JOIN stafferinfo si ON ls.student_number=si.student_number"""
                cur.execute(query)
                staffers = cur.fetchall()
                print(staffers)
                for row in staffers:
                    self.addTable(row)
                cur.close()
            self.flag = 0
        return None

    def opensched(self):
        self.opensched = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.opensched)
        self.opensched.show()

    def setupUi(self, viewwindow):
        self.flag = 1
        viewwindow.setObjectName("viewwindow")
        viewwindow.resize(953, 627)
        viewwindow.setStyleSheet("background:transparent;")
        viewwindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        viewwindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.centralwidget = QtWidgets.QWidget(viewwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, -70, 1011, 701))
        self.label.setObjectName("label")

        self.ctable = QtWidgets.QTableWidget(self.centralwidget)
        self.ctable.setGeometry(QtCore.QRect(230, 60, 631, 441))
        self.ctable.setFrameShape(QtWidgets.QFrame.Box)
        self.ctable.setLineWidth(1)
        self.ctable.setObjectName("ctable")
        self.ctable.setColumnCount(5)
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
        self.ctable.horizontalHeader().setDefaultSectionSize(156)
        self.ctable.horizontalHeader().setMinimumSectionSize(156)
        self.ctable.horizontalHeader().setSortIndicatorShown(False)
        self.ctable.horizontalHeader().setStretchLastSection(False)
        self.ctable.setStyleSheet("Background:White")

        self.Finebut = QtWidgets.QPushButton(self.centralwidget)
        self.Finebut.setGeometry(QtCore.QRect(70, 110, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Nexa Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Finebut.setFont(font)
        self.Finebut.setStyleSheet("QPushButton {background-color: Black} QPushButton:hover {background-color:grey}QPushButton {border-radius:15px}QPushButton {color:White}QPushButton{border:2px solid yellow}QPushButton:pressed{Background-color:yellow};")
        self.Finebut.setObjectName("Finebut")

        self.schedbut = QtWidgets.QPushButton(self.centralwidget)
        self.schedbut.setGeometry(QtCore.QRect(70, 160, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Nexa Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.schedbut.setFont(font)
        self.schedbut.setStyleSheet("QPushButton {background-color: Black} QPushButton:hover {background-color:grey}QPushButton {border-radius:15px}QPushButton {color:White}QPushButton{border:2px solid yellow}QPushButton:pressed{Background-color:yellow};")
        self.schedbut.setObjectName("schedbut")
        self.schedbut.clicked.connect(self.opensched)

        self.exitbut = QtWidgets.QPushButton(self.centralwidget)
        self.exitbut.setGeometry(QtCore.QRect(70, 260, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Nexa Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.exitbut.setFont(font)
        self.exitbut.setStyleSheet("QPushButton {background-color: Black} QPushButton:hover {background-color:grey}QPushButton {border-radius:15px}QPushButton {color:White}QPushButton{border:2px solid yellow}QPushButton:pressed{Background-color:red};")
        self.exitbut.setObjectName("exitbut")
        self.exitbut.clicked.connect(lambda closeFunction: viewwindow.close())

        self.notinbut = QtWidgets.QPushButton(self.centralwidget)
        self.notinbut.setGeometry(QtCore.QRect(70, 210, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Nexa Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.notinbut.setFont(font)
        self.notinbut.setStyleSheet("QPushButton {background-color: Black} QPushButton:hover {background-color:grey}QPushButton {border-radius:15px}QPushButton {color:White}QPushButton{border:2px solid yellow}QPushButton:pressed{Background-color:yellow};")
        self.notinbut.setObjectName("notinbut")

        viewwindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(viewwindow)
        self.statusbar.setObjectName("statusbar")
        viewwindow.setStatusBar(self.statusbar)

        self.retranslateUi(viewwindow)
        QtCore.QMetaObject.connectSlotsByName(viewwindow)

        self.viewStaffer()

    def retranslateUi(self, viewwindow):
        _translate = QtCore.QCoreApplication.translate
        viewwindow.setWindowTitle(_translate("viewwindow", "MainWindow"))
        self.label.setText(_translate("viewwindow", "<html><head/><body><p><img src=\":/login/Pics/Admin-window.png\"width=850 height=500/></p></body></html>"))
        item = self.ctable.horizontalHeaderItem(0)
        item.setText(_translate("viewwindow", "Time in"))
        item = self.ctable.horizontalHeaderItem(1)
        item.setText(_translate("viewwindow", "Time out"))
        item = self.ctable.horizontalHeaderItem(2)
        item.setText(_translate("viewwindow", "Name of staffer"))
        item = self.ctable.horizontalHeaderItem(3)
        item.setText(_translate("viewwindow", "Status"))
        item = self.ctable.horizontalHeaderItem(4)
        item.setText(_translate("viewwindow", "Date"))
        self.Finebut.setText(_translate("viewwindow", "View Fines"))
        self.schedbut.setText(_translate("viewwindow", "Duty Schedules"))
        self.exitbut.setText(_translate("viewwindow", "Exit"))
        self.notinbut.setText(_translate("viewwindow", "Not in duty"))
import dutycheckerFiles_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    viewwindow = QtWidgets.QMainWindow()
    ui = Ui_viewwindow()
    ui.setupUi(viewwindow)
    viewwindow.show()
    sys.exit(app.exec_())

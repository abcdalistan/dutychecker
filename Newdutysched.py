from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox
import pymysql
from newaddwindow_schedwindow import Ui_addwindow
from newupdate_schedwindow import Ui_updatewindow as updatewindow
from newsearchwindow_schedwindow import Ui_searchwindow
from newfinewindow import Ui_MainWindow as finewindow
from PyQt5.QtCore import QCoreApplication,Qt,QBasicTimer,QPoint

class Ui_MainWindow(QMainWindow):
    def cell_was_clicked(self, row, column):
        self.row = row

    def addTable(self,columns):
        rowPosition=self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowPosition)
        for i, column in enumerate(columns):
            self.tableWidget.setItem(rowPosition,i, QtWidgets.QTableWidgetItem(str(column)))

    def viewStaffer(self):
        conn = pymysql.connect('localhost', 'tipvoice', 'password', 'staffer')
        with conn:
            cur = conn.cursor()
            query = ("select si.student_number, s.start_time, s.end_time, si.first_name, s.day, s.semester, s.academic_year from schedules s inner join stafferinfo si on si.student_number=s.student_number")
            cur.execute(query)
            staffers = cur.fetchall()
            for row in staffers:
                self.addTable(row)
            cur.close()
            #adding table when display button is clicked
        return None

    def refreshfunc(self):
        self.tableWidget.setRowCount(0)
        conn = pymysql.connect("localhost", "tipvoice", "password", "staffer")
        with conn:
            cur=conn.cursor()
            query="select si.student_number, s.start_time, s.end_time, si.first_name, s.day, s.semester, s.academic_year from schedules s inner join stafferinfo si on si.student_number=s.student_number"
            cur.execute(query)
            result = cur.fetchall()
            for row in result:
                self.addTable(row)
                cur.close()
        return None

    def addwindow(self):
        self.addwindow = QtWidgets.QMainWindow()
        self.ui = Ui_addwindow()
        self.ui.setupUi(self.addwindow)
        self.addwindow.show()

    def searchWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_searchwindow()
        self.ui.setupUi(self.window)
        self.window.show()

    @QtCore.pyqtSlot()
    def deleteClicked(self):
        try:
            answer = QMessageBox.question(self, "", "Are you sure you want to delete student number '{0}'".format(self.tableWidget.item(self.row, 0).text()))
            if answer == QMessageBox.Yes:
                try:
                    conn = pymysql.connect("localhost", "tipvoice", "password", "staffer")
                    with conn:
                        cur = conn.cursor()
                        query = "DELETE FROM schedules WHERE student_number = \'{0}\'".format(self.tableWidget.item(self.row, 0).text())
                        cur.execute(query)
                        conn.commit()
                        cur.close()
                    self.tableWidget.removeRow(self.row)
                    QMessageBox.about(self, "Delete", "Student number '{0}' has been deleted.".format(self.tableWidget.item(self.row, 0).text()))
                except:
                    pass
            else:
                return
        except:
            pass

    def openUpdateWindow(self):
        try:
            cell_student_number = self.tableWidget.item(self.row, 0).text()
            self.window = QtWidgets.QMainWindow()
            self.ui = updatewindow(self)
            self.ui.setupUi(self.window)
            self.ui.insertData(cell_student_number)
            self.window.show()
        except:
            pass

    def setupUi(self, MainWindow):
        self.MainWindow=MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(948, 562)
        MainWindow.setStyleSheet("background:transparent;")
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, -70, 1011, 701))
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.cellClicked.connect(self.cell_was_clicked)
        self.tableWidget.setGeometry(QtCore.QRect(260, 60, 621, 441))
        self.tableWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        
        self.tableWidget.horizontalHeader().setDefaultSectionSize(140)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.setStyleSheet("Background:White")

        self.addbut = QtWidgets.QPushButton(self.centralwidget)
        self.addbut.setGeometry(QtCore.QRect(90, 100, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Nexa Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.addbut.setFont(font)
        self.addbut.setStyleSheet("QPushButton {background-color: Black} QPushButton:hover {background-color:grey}QPushButton {border-radius:15px}QPushButton {color:White}QPushButton{border:2px solid yellow}QPushButton:pressed{Background-color:yellow};")
        self.addbut.setObjectName("addbut")
        self.addbut.clicked.connect(self.addwindow)

        self.delbut = QtWidgets.QPushButton(self.centralwidget)
        self.delbut.setGeometry(QtCore.QRect(90, 145, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Nexa Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.delbut.setFont(font)
        self.delbut.setStyleSheet("QPushButton {background-color: Black} QPushButton:hover {background-color:grey}QPushButton {border-radius:15px}QPushButton {color:White}QPushButton{border:2px solid yellow}QPushButton:pressed{Background-color:yellow};")
        self.delbut.setObjectName("delbut")
        self.delbut.clicked.connect(self.deleteClicked)

        self.updatebut = QtWidgets.QPushButton(self.centralwidget)
        self.updatebut.setGeometry(QtCore.QRect(90, 190, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Nexa Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.updatebut.setFont(font)
        self.updatebut.setStyleSheet("QPushButton {background-color: Black} QPushButton:hover {background-color:grey}QPushButton {border-radius:15px}QPushButton {color:White}QPushButton{border:2px solid yellow}QPushButton:pressed{Background-color:yellow};")
        self.updatebut.setObjectName("updatebut")
        self.updatebut.clicked.connect(self.openUpdateWindow)

        self.searchbut = QtWidgets.QPushButton(self.centralwidget)
        self.searchbut.setGeometry(QtCore.QRect(90, 235, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Nexa Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.searchbut.setFont(font)
        self.searchbut.setStyleSheet("QPushButton {background-color: Black} QPushButton:hover {background-color:grey}QPushButton {border-radius:15px}QPushButton {color:White}QPushButton{border:2px solid yellow}QPushButton:pressed{Background-color:yellow};")
        self.searchbut.setObjectName("searchbut")
        self.searchbut.clicked.connect(self.searchWindow)

        self.refreshbut = QtWidgets.QPushButton(self.centralwidget)
        self.refreshbut.setGeometry(QtCore.QRect(90, 280, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Nexa Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.refreshbut.setFont(font)
        self.refreshbut.setStyleSheet("QPushButton {background-color: Black} QPushButton:hover {background-color:grey}QPushButton {border-radius:15px}QPushButton {color:White}QPushButton{border:2px solid yellow}QPushButton:pressed{Background-color:yellow};")
        self.refreshbut.setObjectName("refreshbut")
        self.refreshbut.clicked.connect(self.refreshfunc)
        
        self.exitbut = QtWidgets.QPushButton(self.centralwidget)
        self.exitbut.setGeometry(QtCore.QRect(90, 325, 151, 31))
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
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "student number"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Time in"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Time out"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "First name"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Day"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Semester"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Academic year"))

        self.exitbut.setText(_translate("MainWindow", "Exit"))
        self.delbut.setText(_translate("MainWindow", "Delete"))
        self.updatebut.setText(_translate("MainWindow", "Update"))
        self.refreshbut.setText(_translate("MainWindow", "Refresh"))
        self.addbut.setText(_translate("MainWindow", "Add"))
        self.searchbut.setText(_translate("MainWindow", "Search"))
        self.viewStaffer()
import dutycheckerFiles_rc

        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox
import pymysql
from addwindow import Ui_addwindow
from searchwindow import Ui_searchwindow
from viewwindow import Ui_MainWindow as viewwindow
from updatewindow import Ui_updatewindow as updatewindow

class Ui_MainWindow(QMainWindow):

    def cell_was_clicked(self, row, column):
        self.row = row

    def addTable(self,columns):
        rowPosition=self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowPosition)
        for i, column in enumerate(columns):
            self.tableWidget.setItem(rowPosition,i, QtWidgets.QTableWidgetItem(str(column)))

    def viewStaffer(self):
        if self.flag:
            conn = pymysql.connect('localhost', 'tipvoice', 'password', 'staffer')
            with conn:
                cur=conn.cursor()
                query=("SELECT * FROM stafferinfo")
                cur.execute(query)
                result = cur.fetchall()
                for row in result:
                    self.addTable(row)
                cur.close()
            self.flag = 0
            #adding table when display button is clicked

    def refreshfunc(self):
        self.tableWidget.setRowCount(0)
        conn = pymysql.connect('localhost', 'tipvoice', 'password', 'staffer')
        with conn:
            cur=conn.cursor()
            query=("SELECT * FROM stafferinfo")
            cur.execute(query)
            
            result = cur.fetchall()
            for row in result:
                self.addTable(row)
                cur.close()

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
        
    def viewwindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = viewwindow()
        self.ui.setupUi(self.window)
        self.window.show()

# Don't mind about the decorator '@QtCore.pyqtSlot()'
    @QtCore.pyqtSlot()
    def deleteClicked(self):
        try:
            answer = QMessageBox.question(self, "", "Are you sure you want to delete student number '{0}'".format(self.tableWidget.item(self.row, 0).text()))
            if answer == QMessageBox.Yes:
                try:
                    conn = pymysql.connect("localhost", "tipvoice", "password", "staffer")
                    with conn:
                        cur = conn.cursor()
                        query = "DELETE FROM stafferinfo WHERE student_number = \'{0}\'".format(self.tableWidget.item(self.row, 0).text())
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
        else:
            return

    def setupUi(self, MainWindow):
        self.flag = 1
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(995, 759)
        MainWindow.setStyleSheet("background:transparent;")
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 0, 1011, 701))
        self.label.setObjectName("label")

        self.addbut = QtWidgets.QPushButton(self.centralwidget)
        self.addbut.setGeometry(QtCore.QRect(130, 130, 81, 31))
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
        self.delbut.setGeometry(QtCore.QRect(230, 130, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Nexa Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.delbut.setFont(font)
        self.delbut.setStyleSheet("QPushButton {background-color: Black} QPushButton:hover {background-color:grey}QPushButton {border-radius:15px}QPushButton {color:White}QPushButton{border:2px solid yellow}QPushButton:pressed{Background-color:yellow};")
        self.delbut.setObjectName("delbut")
        self.delbut.clicked.connect(self.deleteClicked)

        self.searchbut = QtWidgets.QPushButton(self.centralwidget)
        self.searchbut.setGeometry(QtCore.QRect(330, 130, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Nexa Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.searchbut.setFont(font)
        self.searchbut.setStyleSheet("QPushButton {background-color: Black} QPushButton:hover {background-color:grey}QPushButton {border-radius:15px}QPushButton {color:White}QPushButton{border:2px solid yellow}QPushButton:pressed{Background-color:yellow};")
        self.searchbut.setObjectName("searchbut")
        self.searchbut.clicked.connect(self.searchWindow)

        self.viewbut = QtWidgets.QPushButton(self.centralwidget)
        self.viewbut.setGeometry(QtCore.QRect(430, 130, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Nexa Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.viewbut.setFont(font)
        self.viewbut.setStyleSheet("QPushButton {background-color: Black} QPushButton:hover {background-color:grey}QPushButton {border-radius:15px}QPushButton {color:White}QPushButton{border:2px solid yellow}QPushButton:pressed{Background-color:yellow};")
        self.viewbut.setObjectName("viewbut")
        self.viewbut.clicked.connect(self.viewwindow)

        self.updatebut = QtWidgets.QPushButton(self.centralwidget)
        self.updatebut.setGeometry(QtCore.QRect(530, 130, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Nexa Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.updatebut.setFont(font)
        self.updatebut.setStyleSheet("QPushButton {background-color: Black} QPushButton:hover {background-color:grey}QPushButton {border-radius:15px}QPushButton {color:White}QPushButton{border:2px solid yellow}QPushButton:pressed{Background-color:yellow};")
        self.updatebut.setObjectName("updatebut")
        self.updatebut.clicked.connect(self.openUpdateWindow)

        self.refreshbut = QtWidgets.QPushButton(self.centralwidget)
        self.refreshbut.setGeometry(QtCore.QRect(640, 130, 91, 31))
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
        self.exitbut.setGeometry(QtCore.QRect(750, 130, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Nexa Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.exitbut.setFont(font)
        self.exitbut.setStyleSheet("QPushButton {background-color: Black} QPushButton:hover {background-color:grey}QPushButton {border-radius:15px}QPushButton {color:White}QPushButton{border:2px solid yellow}QPushButton:pressed{Background-color:red};")
        self.exitbut.setObjectName("exitbut")
        self.exitbut.clicked.connect(QtCore.QCoreApplication.instance().quit)

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(110, 180, 771, 381))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setStyleSheet("Background:White")
        self.tableWidget.setColumnCount(5)
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
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(157)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(100)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget.verticalHeader().setMinimumSectionSize(25)
        
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
        self.addbut.setText(_translate("MainWindow", "ADD"))
        self.delbut.setText(_translate("MainWindow", "DELETE"))
        self.searchbut.setText(_translate("MainWindow", "SEARCH"))
        self.viewbut.setText(_translate("MainWindow", "VIEW"))
        self.updatebut.setText(_translate("MainWindow", "UPDATE"))
        self.refreshbut.setText(_translate("MainWindow", "REFRESH"))
        self.exitbut.setText(_translate("MainWindow", "EXIT"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Student no."))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Firstname"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Lastname"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Program"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Position"))
import dutycheckerFiles_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

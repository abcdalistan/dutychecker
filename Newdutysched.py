from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql

class Ui_MainWindow:

    def cell_was_clicked(self, row, column):
        self.row = row
        return None

    def addTable(self,columns):
        rowPosition=self.tablewidget.rowCount()
        self.tablewidget.insertRow(rowPosition)
        for i, column in enumerate(columns):
            self.tablewidget.setItem(rowPosition,i, QtWidgets.QTableWidgetItem(str(column)))
        return None

    def viewStaffer(self):
        if self.flag:
            conn = pymysql.connect('localhost', 'root', '', 'staffer')
            with conn:
                cur = conn.cursor()
                query = ("SELECT ls.login_time, ls.logout_time, si.first_name, ls.status, ls.date FROM loginstaff ls INNER JOIN stafferinfo si on ls.student_number=si.student_number WHERE ls.status = 1")
                cur.execute(query)
                staffers = cur.fetchall()
                print(staffers)
                for row in staffers:
                    self.addTable(row)
                cur.close()
            self.flag = 0
            #adding table when display button is clicked
        return None

    def refreshfunc(self):
        self.ctable.setRowCount(0)
        conn = pymysql.connect('localhost', 'root', '', 'staffer')
        with conn:
            cur=conn.cursor()
            query=("SELECT  FROM schedule s INNER JOIN  si on ls.student_number=si.student_number")
            cur.execute(query)
            result = cur.fetchall()
            for row in result:
                self.addTable(row)
                cur.close()
        return None

    def setupUi(self, MainWindow):
        
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
        self.tableWidget.setGeometry(QtCore.QRect(260, 60, 621, 441))
        self.tableWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setObjectName("tableWidget")
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
        self.tableWidget.horizontalHeader().setDefaultSectionSize(140)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.setStyleSheet("Background:White")

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(110, 100, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Nexa Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setStyleSheet("Background:white")

        self.exitbut = QtWidgets.QPushButton(self.centralwidget)
        self.exitbut.setGeometry(QtCore.QRect(90, 190, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Nexa Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.exitbut.setFont(font)
        self.exitbut.setStyleSheet("QPushButton {background-color: Black} QPushButton:hover {background-color:grey}QPushButton {border-radius:15px}QPushButton {color:White}QPushButton{border:2px solid yellow}QPushButton:pressed{Background-color:red};")
        self.exitbut.setObjectName("exitbut")
        self.exitbut.clicked.connect(lambda closeFunction: MainWindow.close())

        self.addbut = QtWidgets.QPushButton(self.centralwidget)
        self.addbut.setGeometry(QtCore.QRect(90, 150, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Nexa Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.addbut.setFont(font)
        self.addbut.setStyleSheet("QPushButton {background-color: Black} QPushButton:hover {background-color:grey}QPushButton {border-radius:15px}QPushButton {color:White}QPushButton{border:2px solid yellow}QPushButton:pressed{Background-color:yellow};")
        self.addbut.setObjectName("addbut")
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
        item.setText(_translate("MainWindow", "Time in"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Time out"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Name of staffer"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Program"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Position"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Monday"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Tuesday"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Wednesday"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Thursday"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Friday"))
        self.exitbut.setText(_translate("MainWindow", "Exit"))
        self.addbut.setText(_translate("MainWindow", "Add"))
import dutycheckerFiles_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

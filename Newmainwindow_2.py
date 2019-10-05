from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox
import pymysql
from Newlogin import Ui_adminlogin
from datetime import datetime

class Ui_MainWindow(QMainWindow): 

    def clear(self):
        self.namebox.setText("")
        self.programbox.setText("")
        self.posbox.setText("")

    def login(self):
        conn = pymysql.connect('localhost', 'root', '', 'staffer')
        student_number=self.idbox.text()
        with conn:
            cur=conn.cursor()
            query = "SELECT * FROM stafferinfo"
            cur.execute(query)
            result = cur.fetchall()
            accounts = {}
            for account_number in range(0, len(result)):
                accounts[result[account_number][0]] = result[account_number]
            if (student_number in accounts):
                query = "SELECT * FROM stafferinfo where student_number= \"{}\"".format(student_number)
                cur.execute(query)
                result = cur.fetchone()
                self.namebox.setText(" ".join([result[1], result[2]]))
                self.programbox.setText(result[3])
                self.posbox.setText(result[4])
                self.time = datetime.now()
                QMessageBox.about(self, "Login", result[1] +", you have successfully logged in!\nTime: {0}".format(self.displaytime()))
        return None
        
    def exit(self):
        sys.exit()
        return None

    def displaytime(self):
        self.time = datetime.now()
        return "{0}:{1}:{2}".format(self.time.hour, self.time.minute, self.time.second)



    def loggedin(self):
        conn = pymysql.connect('localhost', 'root', '', 'staffer')
        student_number=self.idbox.text()
        now = self.time = datetime.now()
        current_date = now.strftime("%y-%m-%d")
        current_time = now.strftime("%H:%M:%S")
        with conn:
            cur=conn.cursor()
            query = "SELECT * FROM stafferinfo"
            cur.execute(query)
            result = cur.fetchall()
            accounts = {}
            for account_number in range(0, len(result)):
                accounts[result[account_number][0]] = result[account_number]
            if (student_number in accounts):
                # Checks if the student number exists in the loginstaff table, otherwise, insert a new one
                if self.checkStaffer(student_number):
                    QMessageBox.about(self, "Login", "{0} already logged in!".format(student_number))
                else:
                    self.login() # Invokes the login method
                    cur.execute("INSERT INTO loginstaff (student_number, login_time, status, date) values (\"{0}\",\"{1}\", \"{2}\", \"{3}\")".format(student_number, current_time, 1, current_date))
            elif (self.idbox.text() == ""):
                QMessageBox.about(self, "Empty", "Input student number")
                self.clear()
            elif (self.idbox.text().isalpha()):
                QMessageBox.about(self, "Numbers only", "Positive integer numbers only")
                self.clear()
            else:
                QMessageBox.about(self, "Does not exist", "Student number does not exist")
                self.clear()
        return None

    # Checks if the given student number exists in the loginstaff table
    def checkStaffer(self, student_number):
        conn = pymysql.connect('localhost', 'tipvoice', 'password', 'staffer')
        with conn:
            cur = conn.cursor()
            query = "SELECT student_number FROM loginstaff"
            cur.execute(query)
            result = cur.fetchall()
            staffers = []
            for stud_num in result:
                staffers.append(stud_num[0])
            if student_number in staffers:
                return 1
            else:
                return 0
        return None

    def logout(self):
        conn = pymysql.connect('localhost', 'tipvoice', 'password', 'staffer')
        student_number=self.idbox.text()
        now = self.time = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        with conn:
            cur=conn.cursor()
            query = "SELECT * FROM stafferinfo"
            cur.execute(query)
            result = cur.fetchall()
            accounts = {}
            for account_number in range(0, len(result)):
                accounts[result[account_number][0]] = result[account_number]
            if (student_number in accounts):
                query = "SELECT * FROM stafferinfo where student_number= \"{}\"".format(student_number)
                cur.execute(query)
                result = cur.fetchone()
                self.namebox.setText(" ".join([result[1], result[2]]))
                self.programbox.setText(result[3])
                self.posbox.setText(result[4])
                self.time = datetime.now()
                QMessageBox.about(self, "Logout", result[1] +", you have successfully logged out!\nTime: {0}".format(self.displaytime()))
        return None

    def loggedout(self):
        conn = pymysql.connect('localhost', 'tipvoice', 'password', 'staffer')
        student_number=self.idbox.text()
        now = self.time = datetime.now()
        current_date = now.strftime("%y-%m-%d")
        current_time = now.strftime("%H:%M:%S")
        with conn:
            cur=conn.cursor()
            query = "SELECT * FROM loginstaff"
            cur.execute(query)
            result = cur.fetchall()
            accounts = {}
            for account_number in range(0, len(result)):
                accounts[result[account_number][0]] = result[account_number]
            if (student_number in accounts): 
                if self.checkStaffer(student_number):
                    QMessageBox.about(self, "Logout", "{0} already logged out!".format(student_number))
                else:
                    self.logout()
                    cur.execute("UPDATE loginstaff SET logout_time = '{0}' where student_number=\"{1}\"".format(current_time, student_number))
                    self.clear()
            elif (self.idbox.text() == ""):
                QMessageBox.about(self, "Empty", "Input student number")
                self.clear()
            elif (self.idbox.text().isalpha()):
                QMessageBox.about(self, "Numbers only", "Positive integer numbers only")
                self.clear()
            else:
                QMessageBox.about(self, "Does not exist", "Student number does not exist")
                self.clear()
        return None

    def adminwindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_adminlogin()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(581, 641)
        MainWindow.setStyleSheet("background:transparent;")
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.idbox = QtWidgets.QLineEdit(self.centralwidget)
        self.idbox.setGeometry(QtCore.QRect(180, 380, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Nexa Light")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.idbox.setFont(font)
        self.idbox.setAlignment(QtCore.Qt.AlignCenter)
        self.idbox.setStyleSheet("Background:white")
        self.idbox.setObjectName("idbox")

        self.loginbut = QtWidgets.QPushButton(self.centralwidget)
        self.loginbut.setGeometry(QtCore.QRect(220, 430, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Nexa Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.loginbut.setFont(font)
        self.loginbut.setStyleSheet("QPushButton {background-color: Black} QPushButton:hover {background-color:grey}QPushButton {border-radius:15px}QPushButton {color:White}QPushButton{border:2px solid yellow}QPushButton:pressed{Background-color:yellow};")
        self.loginbut.setObjectName("loginbut")
        self.loginbut.clicked.connect(self.loggedin)

        self.logoutbut = QtWidgets.QPushButton(self.centralwidget)
        self.logoutbut.setGeometry(QtCore.QRect(220, 470, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Nexa Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.logoutbut.setFont(font)
        self.logoutbut.setStyleSheet("QPushButton {background-color: Black} QPushButton:hover {background-color:grey}QPushButton {border-radius:15px}QPushButton {color:White}QPushButton{border:2px solid yellow}QPushButton:pressed{Background-color:yellow};")
        self.logoutbut.setObjectName("logoutbut")
        self.logoutbut.clicked.connect(self.loggedout)

        self.adminbut = QtWidgets.QPushButton(self.centralwidget)
        self.adminbut.setGeometry(QtCore.QRect(220, 510, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Nexa Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.adminbut.setFont(font)
        self.adminbut.setStyleSheet("QPushButton {background-color: Black} QPushButton:hover {background-color:grey}QPushButton{border-radius:15px}QPushButton{color:white}QPushButton{border:2px solid yellow}QPushButton:pressed{background-color:yellow};")
        self.adminbut.setObjectName("adminbut")
        self.adminbut.clicked.connect(self.adminwindow)

        self.exitbut = QtWidgets.QPushButton(self.centralwidget)
        self.exitbut.setGeometry(QtCore.QRect(220, 550, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Nexa Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.exitbut.setFont(font)
        self.exitbut.setStyleSheet("QPushButton {background-color: Black} QPushButton:hover {background-color:grey}QPushButton{border-radius:15px}QPushButton{color:white}QPushButton{border:2px solid yellow}QPushButton:pressed{background-color:red};")
        self.exitbut.setObjectName("exitbut")
        self.exitbut.clicked.connect(self.exit)

        self.namebox = QtWidgets.QLineEdit(self.centralwidget)
        self.namebox.setGeometry(QtCore.QRect(110, 230, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Nexa Light")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.namebox.setFont(font)
        self.namebox.setAlignment(QtCore.Qt.AlignCenter)
        self.namebox.setReadOnly(True)
        self.namebox.setStyleSheet("background:white")
        self.namebox.setObjectName("namebox")
        
        self.programbox = QtWidgets.QLineEdit(self.centralwidget)
        self.programbox.setGeometry(QtCore.QRect(110, 280, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Nexa Light")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.programbox.setFont(font)
        self.programbox.setAlignment(QtCore.Qt.AlignCenter)
        self.programbox.setReadOnly(True)
        self.programbox.setStyleSheet("background:white")
        self.programbox.setObjectName("programbox")

        self.posbox = QtWidgets.QLineEdit(self.centralwidget)
        self.posbox.setGeometry(QtCore.QRect(110, 330, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Nexa Light")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.posbox.setFont(font)
        self.posbox.setAlignment(QtCore.Qt.AlignCenter)
        self.posbox.setReadOnly(True)
        self.posbox.setStyleSheet("background:White")
        self.posbox.setObjectName("posbox")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, -20, 521, 641))
        self.label.setObjectName("label")
        self.Time = QtWidgets.QLabel(self.centralwidget)
        self.Time.setGeometry(QtCore.QRect(75, 520, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Nexa Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Time.setFont(font)
        self.Time.setStyleSheet("color: rgb(255, 255, 0);")
        self.Time.setObjectName("Time")

        self.Date = QtWidgets.QLabel(self.centralwidget)
        self.Date.setGeometry(QtCore.QRect(75, 550, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Nexa Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Date.setFont(font)
        self.Date.setStyleSheet("color: rgb(255, 255, 0);")
        self.Date.setObjectName("Date")
        self.label.raise_()
        self.namebox.raise_()
        self.programbox.raise_()
        self.posbox.raise_()
        self.idbox.raise_()
        self.loginbut.raise_()
        self.logoutbut.raise_()
        self.adminbut.raise_()
        self.Time.raise_()
        self.Date.raise_()
        self.exitbut.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        MainWindow.keyPressEvent = self.defineKeyPressEvent
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def defineKeyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Return:
            self.loggedin()
        if e.key() == QtCore.Qt.Key_Enter:
            self.loggedin()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.namebox.setPlaceholderText(_translate("MainWindow", "Name"))
        self.programbox.setPlaceholderText(_translate("MainWindow", "Program"))
        self.posbox.setPlaceholderText(_translate("MainWindow", "Position"))
        self.idbox.setPlaceholderText(_translate("MainWindow", "Enter student ID"))
        self.adminbut.setText(_translate("MainWindow", "Admin"))
        self.loginbut.setText(_translate("MainWindow", "Login"))
        self.logoutbut.setText(_translate("MainWindow", "Logout"))
        self.exitbut.setText(_translate("MainWindow","Exit"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/login/Pics/Main-window.png\"width=561 height=641/></p></body></html>"))
        self.Time.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">TIME:</span></p></body></html>"))
        self.Date.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">DATE:</span></p></body></html>"))
import dutycheckerFiles_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

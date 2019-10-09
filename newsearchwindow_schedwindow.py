from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox
import pymysql
from datetime import datetime

class Ui_searchwindow(QMainWindow):
    def searchstaffer(self):
        conn = pymysql.connect('localhost', 'tipvoice', 'password', 'staffer')
        name=self.namebox.text()
        if (name==''):
            QMessageBox.about(self, "Empty", "Input first name")
            return

        with conn:
            cur=conn.cursor()
            query = "SELECT * FROM schedules"
            cur.execute(query)
            result = cur.fetchall()
            accounts = {}
            for account_number in range(0, 2):
                accounts[result[account_number][0]] = result[account_number]
                for student_number in accounts:
                    if (student_number in accounts):
                        cur.execute("SELECT * FROM stafferinfo where first_name= \"{}\"".format(name))
                        result= cur.fetchone()
                        self.idbox.setText(accounts[student_number][0])
                        self.tinbox.setText((datetime.min + accounts[student_number][1]).time().strftime('%H:%M:%S'))
                        self.toutbox.setText((datetime.min + accounts[student_number][2]).time().strftime('%H:%M:%S'))
                        self.daybox.setText(accounts[student_number][3])
                        self.sembox.setText(accounts[student_number][4])
                        self.aybox.setText(accounts[student_number][5])
                        break
                    else:
                        QMessageBox.about(self, "Does not exist", "Staffer does not exist")

    def setupUi(self, searchwindow):
        searchwindow.setObjectName("searchwindow")
        searchwindow.resize(800, 600)
        searchwindow.setStyleSheet("background:transparent;")
        searchwindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        searchwindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.centralwidget = QtWidgets.QWidget(searchwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 20, 581, 571))
        self.label.setObjectName("label")

        self.namebox = QtWidgets.QLineEdit(self.centralwidget)
        self.namebox.setGeometry(QtCore.QRect(240, 250, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Nexa Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.namebox.setFont(font)
        self.namebox.setAlignment(QtCore.Qt.AlignCenter)
        self.namebox.setObjectName("namebox")
        self.namebox.setStyleSheet("Background:White")

        self.idbox = QtWidgets.QLineEdit(self.centralwidget)
        self.idbox.setGeometry(QtCore.QRect(240, 290, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Nexa Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.idbox.setFont(font)
        self.idbox.setAlignment(QtCore.Qt.AlignCenter)
        self.idbox.setObjectName("idbox")
        self.idbox.setStyleSheet("Background:white")
        self.idbox.setReadOnly(True)      

        self.tinbox = QtWidgets.QLineEdit(self.centralwidget)
        self.tinbox.setGeometry(QtCore.QRect(240, 330, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Nexa Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tinbox.setFont(font)
        self.tinbox.setAlignment(QtCore.Qt.AlignCenter)
        self.tinbox.setObjectName("tinbox")
        self.tinbox.setStyleSheet("Background:white")
        self.tinbox.setReadOnly(True)

        self.toutbox = QtWidgets.QLineEdit(self.centralwidget)
        self.toutbox.setGeometry(QtCore.QRect(240, 370, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Nexa Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.toutbox.setFont(font)
        self.toutbox.setText("")
        self.toutbox.setAlignment(QtCore.Qt.AlignCenter)
        self.toutbox.setObjectName("toutbox")
        self.toutbox.setStyleSheet("Background:White")
        self.toutbox.setReadOnly(True)

        self.daybox = QtWidgets.QLineEdit(self.centralwidget)
        self.daybox.setGeometry(QtCore.QRect(240, 410, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Nexa Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.daybox.setFont(font)
        self.daybox.setAlignment(QtCore.Qt.AlignCenter)
        self.daybox.setObjectName("daybox")
        self.daybox.setStyleSheet("Background:white")
        self.daybox.setReadOnly(True)

        self.sembox = QtWidgets.QLineEdit(self.centralwidget)
        self.sembox.setGeometry(QtCore.QRect(240, 450, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Nexa Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.sembox.setFont(font)
        self.sembox.setAlignment(QtCore.Qt.AlignCenter)
        self.sembox.setObjectName("daybox")
        self.sembox.setStyleSheet("Background:white")
        self.sembox.setReadOnly(True)

        self.aybox = QtWidgets.QLineEdit(self.centralwidget)
        self.aybox.setGeometry(QtCore.QRect(240, 490, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Nexa Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.aybox.setFont(font)
        self.aybox.setAlignment(QtCore.Qt.AlignCenter)
        self.aybox.setObjectName("aybox")
        self.aybox.setStyleSheet("Background:white")
        self.aybox.setReadOnly(True)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(290, 535, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Nexa Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {background-color: Black} QPushButton:hover {background-color:grey}QPushButton {border-radius:15px}QPushButton {color:White}QPushButton{border:2px solid yellow}QPushButton:pressed{Background-color:yellow};")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.searchstaffer)

        self.exitbut = QtWidgets.QPushButton(self.centralwidget)
        self.exitbut.setGeometry(QtCore.QRect(400, 535, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Nexa Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.exitbut.setFont(font)
        self.exitbut.setStyleSheet("QPushButton {background-color: Black} QPushButton:hover {background-color:grey}QPushButton {border-radius:15px}QPushButton {color:White}QPushButton{border:2px solid yellow}QPushButton:pressed{Background-color:red};")
        self.exitbut.setObjectName("exitbut")
        self.exitbut.clicked.connect(lambda closeFunction: searchwindow.close())
        searchwindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(searchwindow)
        self.statusbar.setObjectName("statusbar")
        searchwindow.setStatusBar(self.statusbar)

        self.retranslateUi(searchwindow)
        QtCore.QMetaObject.connectSlotsByName(searchwindow)

    def retranslateUi(self, searchwindow):
        _translate = QtCore.QCoreApplication.translate
        searchwindow.setWindowTitle(_translate("searchwindow", "MainWindow"))
        self.label.setText(_translate("addwindow", "<html><head/><body><p><img src=\":/login/Pics/Login-window.png\"width=522 height=560/></p></body></html>"))
        self.idbox.setPlaceholderText(_translate("addwindow", "Enter ID"))
        self.tinbox.setPlaceholderText(_translate("addwindow", "Enter Time In"))
        self.toutbox.setPlaceholderText(_translate("addwindow", "Enter Time out"))
        self.namebox.setPlaceholderText(_translate("addwindow", "Enter First Name"))
        self.daybox.setPlaceholderText(_translate("addwindow", "Enter Day"))
        self.sembox.setPlaceholderText(_translate("addwindow", "Enter Semester"))
        self.aybox.setPlaceholderText(_translate("addwindow", "Enter School Year"))
        self.pushButton.setText(_translate("searchwindow", "SEARCH"))
        self.exitbut.setText(_translate("searchwindow", "EXIT"))
import dutycheckerFiles_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    searchwindow = QtWidgets.QMainWindow()
    ui = Ui_searchwindow()
    ui.setupUi(searchwindow)
    searchwindow.show()
    sys.exit(app.exec_())

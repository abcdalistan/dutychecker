from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox
import pymysql


class Ui_searchwindow(QMainWindow):

    def searchstaffer(self):
        conn = pymysql.connect('localhost', 'tipvoice', 'password', 'staffer')
        student_number=self.idbox.text()
        last_name=self.lnamebox.text()
        if (last_name==''):
            QMessageBox.about(self, "Empty", "Input last name")
            return
        with conn:
            cur=conn.cursor()
            query = "SELECT * FROM stafferinfo"
            cur.execute(query)
            result = cur.fetchall()
            accounts = {}
            for account_number in range(0, 5):
                accounts[result[account_number][0]] = result[account_number]
                for student_number in accounts:
                    if (student_number in accounts):
                        query = "SELECT * FROM stafferinfo where last_name= \"{}\"".format(last_name)
                        cur.execute(query)
                        result = cur.fetchone()
                        self.idbox.setText(result[0])
                        self.fnamebox.setText(result[1])
                        self.cbox.setText(result[3])
                        self.posbox.setText(result[4])
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
        self.label.setGeometry(QtCore.QRect(120, 20, 581, 511))
        self.label.setObjectName("label")

        self.lnamebox = QtWidgets.QLineEdit(self.centralwidget)
        self.lnamebox.setGeometry(QtCore.QRect(240, 250, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Nexa Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lnamebox.setFont(font)
        self.lnamebox.setAlignment(QtCore.Qt.AlignCenter)
        self.lnamebox.setObjectName("lnamebox")
        self.lnamebox.setStyleSheet("Background:white")

        self.fnamebox = QtWidgets.QLineEdit(self.centralwidget)
        self.fnamebox.setGeometry(QtCore.QRect(240, 290, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Nexa Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.fnamebox.setFont(font)
        self.fnamebox.setAlignment(QtCore.Qt.AlignCenter)
        self.fnamebox.setObjectName("fnamebox")
        self.fnamebox.setStyleSheet("Background:white")
        self.fnamebox.setReadOnly(True)

        self.idbox = QtWidgets.QLineEdit(self.centralwidget)
        self.idbox.setGeometry(QtCore.QRect(240, 330, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Nexa Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.idbox.setFont(font)
        self.idbox.setText("")
        self.idbox.setAlignment(QtCore.Qt.AlignCenter)
        self.idbox.setObjectName("idbox")
        self.idbox.setStyleSheet("Background:White")
        self.idbox.setReadOnly(True)
        

        self.cbox = QtWidgets.QLineEdit(self.centralwidget)
        self.cbox.setGeometry(QtCore.QRect(240, 370, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Nexa Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cbox.setFont(font)
        self.cbox.setAlignment(QtCore.Qt.AlignCenter)
        self.cbox.setObjectName("cbox")
        self.cbox.setStyleSheet("Background:White")
        self.cbox.setReadOnly(True)

        self.posbox = QtWidgets.QLineEdit(self.centralwidget)
        self.posbox.setGeometry(QtCore.QRect(240, 410, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Nexa Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.posbox.setFont(font)
        self.posbox.setAlignment(QtCore.Qt.AlignCenter)
        self.posbox.setObjectName("posbox")
        self.posbox.setStyleSheet("Background:white")
        self.posbox.setReadOnly(True)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(290, 450, 91, 31))
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
        self.exitbut.setGeometry(QtCore.QRect(400, 450, 91, 31))
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
        self.label.setText(_translate("searchwindow", "<html><head/><body><p><img src=\":/login/Pics/Login-window.png\"width=522 height=484/></p></body></html>"))
        self.fnamebox.setPlaceholderText(_translate("searchwindow", "Enter First Name"))
        self.lnamebox.setPlaceholderText(_translate("searchwindow", "Enter Last Name"))
        self.idbox.setPlaceholderText(_translate("searchwindow", "Enter ID"))
        self.cbox.setPlaceholderText(_translate("searchwindow", "Enter Program"))
        self.posbox.setPlaceholderText(_translate("searchwindow", "Enter Position"))
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

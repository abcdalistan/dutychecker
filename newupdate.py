from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox
import pymysql

class Ui_updatewindow(QMainWindow):
    def insertData(self, cell_student_number):
        conn = pymysql.connect("localhost", "tipvoice", "password", "staffer")
        cur = conn.cursor()
        query = "SELECT * FROM stafferinfo"
        cur.execute(query)
        result = cur.fetchall()
        accounts = {}
        for account_number in range(0, len(result)):
            accounts[result[account_number][0]] = result[account_number]
        for student_number in accounts:
            if (student_number == cell_student_number):
                self.idbox.setText(accounts[student_number][0])
                self.fnamebox.setText(accounts[student_number][1])
                self.lnamebox.setText(accounts[student_number][2])
                self.posbox.setText(accounts[student_number][4])
                self.cbox.setText(accounts[student_number][3])
                break
        self.cell_student_number = cell_student_number

    def updateData(self):
        conn = pymysql.connect("localhost", "tipvoice", "password", "staffer")
        cur = conn.cursor()
        idbox=self.idbox.text()
        fname = self.fnamebox.text()
        lname = self.lnamebox.text()
        posbox = self.posbox.text()
        cbox = self.cbox.text()
        selected_account = [idbox, fname, lname, cbox, posbox, self.cell_student_number]
        query = "UPDATE stafferinfo SET student_number=\"{0}\", first_name=\"{1}\", last_name=\"{2}\", program=\"{3}\", position=\"{4}\" WHERE student_number = \"{5}\"".format(*selected_account)
        QMessageBox.about(self, "Updated", "Updated!")
        cur.execute(query)
        conn.commit()

    def setupUi(self, updatewindow):
        updatewindow.setObjectName("updatewindow")
        updatewindow.resize(800, 600)
        updatewindow.setStyleSheet("background:transparent;")
        updatewindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        updatewindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.centralwidget = QtWidgets.QWidget(updatewindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 20, 581, 511))
        self.label.setObjectName("label")

        self.idbox = QtWidgets.QLineEdit(self.centralwidget)
        self.idbox.setGeometry(QtCore.QRect(240, 240, 311, 31))
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

        self.fnamebox = QtWidgets.QLineEdit(self.centralwidget)
        self.fnamebox.setGeometry(QtCore.QRect(240, 280, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Nexa Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.fnamebox.setFont(font)
        self.fnamebox.setAlignment(QtCore.Qt.AlignCenter)
        self.fnamebox.setObjectName("fnamebox")
        self.fnamebox.setStyleSheet("Background:White")

        self.lnamebox = QtWidgets.QLineEdit(self.centralwidget)
        self.lnamebox.setGeometry(QtCore.QRect(240, 320, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Nexa Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lnamebox.setFont(font)
        self.lnamebox.setAlignment(QtCore.Qt.AlignCenter)
        self.lnamebox.setObjectName("lnamebox")
        self.lnamebox.setStyleSheet("Background:White")

        self.cbox = QtWidgets.QLineEdit(self.centralwidget)
        self.cbox.setGeometry(QtCore.QRect(240, 360, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Nexa Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cbox.setFont(font)
        self.cbox.setAlignment(QtCore.Qt.AlignCenter)
        self.cbox.setObjectName("cbox")
        self.cbox.setStyleSheet("Background:White")

        self.posbox = QtWidgets.QLineEdit(self.centralwidget)
        self.posbox.setGeometry(QtCore.QRect(240, 400, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Nexa Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.posbox.setFont(font)
        self.posbox.setAlignment(QtCore.Qt.AlignCenter)
        self.posbox.setObjectName("posbox")
        self.posbox.setStyleSheet("Background:White")

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
        self.pushButton.clicked.connect(self.updateData)

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
        self.exitbut.clicked.connect(lambda closeFunction: updatewindow.close())

        updatewindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(updatewindow)
        self.statusbar.setObjectName("statusbar")
        updatewindow.setStatusBar(self.statusbar)

        self.retranslateUi(updatewindow)
        QtCore.QMetaObject.connectSlotsByName(updatewindow)

    def retranslateUi(self, updatewindow):
        _translate = QtCore.QCoreApplication.translate
        updatewindow.setWindowTitle(_translate("updatewindow", "MainWindow"))
        self.label.setText(_translate("updatewindow", "<html><head/><body><p><img src=\":/login/Pics/Login-window.png\"width=522 height=484/></p></body></html>"))
        self.fnamebox.setPlaceholderText(_translate("updatewindow", "Enter First Name"))
        self.lnamebox.setPlaceholderText(_translate("updatewindow", "Enter Last Name"))
        self.idbox.setPlaceholderText(_translate("updatewindow", "Enter ID"))
        self.cbox.setPlaceholderText(_translate("updatewindow", "Enter Program"))
        self.posbox.setPlaceholderText(_translate("updatewindow", "Enter Position"))
        self.pushButton.setText(_translate("updatewindow", "CONFIRM"))
        self.exitbut.setText(_translate("updatewindow", "EXIT"))
import dutycheckerFiles_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    updatewindow = QtWidgets.QMainWindow()
    ui = Ui_updatewindow()
    ui.setupUi(updatewindow)
    updatewindow.show()
    sys.exit(app.exec_())

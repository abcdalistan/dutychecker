from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox
import pymysql


class Ui_addwindow(QMainWindow):

    def addStaffer(self):
        conn = pymysql.connect('localhost', 'tipvoice', 'password', 'staffer')
        student_number = self.idbox.text()
        first_name = self.fnamebox.text()
        last_name = self.lnamebox.text()
        program = self.cbox.text()
        position = self.posbox.text()
        if (student_number=='' or first_name=='' or last_name=='' or program=='' or position==''):
            QMessageBox.about(self, 'Warning!', "Please fill up all information")
            return
        with conn:
            cur = conn.cursor()
            query = "SELECT * FROM stafferinfo;"
            cur.execute(query)
            result = tuple(cur.fetchall())
            accounts = {}
            for account_number in range(0, len(result)):
                accounts[result[account_number][0]] = result[account_number]
            # ISSUE: Find and fix the possible issues for these conditions (If any)
            if (student_number in accounts):
                if (first_name == accounts[student_number][1] and last_name == accounts[student_number][2] and program == accounts[student_number][3] and position == accounts[student_number][4]):
                    QMessageBox.about(self, 'Warning', 'Staffer already exist!')
                else:
                    QMessageBox.about(self, 'Warning', 'Staffer already exist!')
            else:
                query = "INSERT INTO stafferinfo values (\"{0}\", \"{1}\", \"{2}\", \"{3}\", \"{4}\")".format(student_number, first_name, last_name, program, position)
                cur.execute(query)
                QMessageBox.about(self, 'Add Staffer!', "Successfully Added the staffer!")
                conn.commit()
        return

    def setupUi(self, addwindow):
        addwindow.setObjectName("addwindow")
        addwindow.resize(800, 600)
        addwindow.setStyleSheet("background:transparent;")
        addwindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        addwindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.centralwidget = QtWidgets.QWidget(addwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 20, 581, 511))
        self.label.setObjectName("label")
        self.fnamebox = QtWidgets.QLineEdit(self.centralwidget)
        self.fnamebox.setGeometry(QtCore.QRect(240, 250, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Nexa Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.fnamebox.setFont(font)
        self.fnamebox.setAlignment(QtCore.Qt.AlignCenter)
        self.fnamebox.setObjectName("fnamebox")
        self.fnamebox.setStyleSheet("Background:white")

        self.lnamebox = QtWidgets.QLineEdit(self.centralwidget)
        self.lnamebox.setGeometry(QtCore.QRect(240, 290, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Nexa Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lnamebox.setFont(font)
        self.lnamebox.setAlignment(QtCore.Qt.AlignCenter)
        self.lnamebox.setObjectName("lnamebox")
        self.lnamebox.setStyleSheet("Background:white")

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
        self.pushButton.clicked.connect(self.addStaffer)

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
        self.exitbut.clicked.connect(lambda closeFunction: addwindow.close())

        addwindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(addwindow)
        self.statusbar.setObjectName("statusbar")
        addwindow.setStatusBar(self.statusbar)

        self.retranslateUi(addwindow)
        QtCore.QMetaObject.connectSlotsByName(addwindow)

    def retranslateUi(self, addwindow):
        _translate = QtCore.QCoreApplication.translate
        addwindow.setWindowTitle(_translate("addwindow", "MainWindow"))
        self.label.setText(_translate("addwindow", "<html><head/><body><p><img src=\":/login/Pics/Login-window.png\"width=522 height=484/></p></body></html>"))
        self.fnamebox.setPlaceholderText(_translate("addwindow", "Enter First Name"))
        self.lnamebox.setPlaceholderText(_translate("addwindow", "Enter Last Name"))
        self.idbox.setPlaceholderText(_translate("addwindow", "Enter ID"))
        self.cbox.setPlaceholderText(_translate("addwindow", "Enter Program"))
        self.posbox.setPlaceholderText(_translate("addwindow", "Enter Position"))
        self.pushButton.setText(_translate("addwindow", "CONFIRM"))
        self.exitbut.setText(_translate("addwindow", "EXIT"))
import dutycheckerFiles_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    addwindow = QtWidgets.QMainWindow()
    ui = Ui_addwindow()
    ui.setupUi(addwindow)
    addwindow.show()
    sys.exit(app.exec_())

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox
import pymysql


class Ui_addwindow(QMainWindow):

    def addStaffer(self):
        try:
            conn = pymysql.connect('localhost', 'tipvoice', 'password', 'staffer')
            student_number = self.idbox.text()
            start_time= self.tinbox.text()
            end_time= self.toutbox.text()
            day= self.daybox.text()
            sem=self.sembox.text()
            acadyear=self.aybox.text()
            if (student_number=='' or start_time=='' or end_time=='' or day=='' or acadyear=='' or sem==''):
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
                try:
                    query = "INSERT INTO schedules values (\"{0}\", \"{1}\", \"{2}\", \"{3}\", \"{4}\",\"{5}\")".format(student_number, start_time, end_time, day, sem, acadyear)
                    cur.execute(query)
                    QMessageBox.about(self, 'Add Schedule!', "Successfully Added the schedule!")
                    conn.commit()
                except:
                    QMessageBox.about(self, 'Add Schedule', 'Student does not exist')
        except:
            print('Error')
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
        self.label.setGeometry(QtCore.QRect(120, 20, 581, 550))
        self.label.setObjectName("label")
        
        self.idbox = QtWidgets.QLineEdit(self.centralwidget)
        self.idbox.setGeometry(QtCore.QRect(240, 250, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Nexa Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.idbox.setFont(font)
        self.idbox.setAlignment(QtCore.Qt.AlignCenter)
        self.idbox.setObjectName("idbox")
        self.idbox.setStyleSheet("Background:white")

        self.tinbox = QtWidgets.QLineEdit(self.centralwidget)
        self.tinbox.setGeometry(QtCore.QRect(240, 290, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Nexa Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tinbox.setFont(font)
        self.tinbox.setAlignment(QtCore.Qt.AlignCenter)
        self.tinbox.setObjectName("tinbox")
        self.tinbox.setStyleSheet("Background:white")

        self.toutbox = QtWidgets.QLineEdit(self.centralwidget)
        self.toutbox.setGeometry(QtCore.QRect(240, 330, 311, 31))
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

        self.daybox = QtWidgets.QLineEdit(self.centralwidget)
        self.daybox.setGeometry(QtCore.QRect(240, 370, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Nexa Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.daybox.setFont(font)
        self.daybox.setAlignment(QtCore.Qt.AlignCenter)
        self.daybox.setObjectName("daybox")
        self.daybox.setStyleSheet("Background:white")

        self.sembox = QtWidgets.QLineEdit(self.centralwidget)
        self.sembox.setGeometry(QtCore.QRect(240, 410, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Nexa Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.sembox.setFont(font)
        self.sembox.setAlignment(QtCore.Qt.AlignCenter)
        self.sembox.setObjectName("daybox")
        self.sembox.setStyleSheet("Background:white")        

        self.aybox = QtWidgets.QLineEdit(self.centralwidget)
        self.aybox.setGeometry(QtCore.QRect(240, 450, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Nexa Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.aybox.setFont(font)
        self.aybox.setAlignment(QtCore.Qt.AlignCenter)
        self.aybox.setObjectName("aybox")
        self.aybox.setStyleSheet("Background:white")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(290, 500, 91, 31))
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
        self.exitbut.setGeometry(QtCore.QRect(400, 500, 91, 31))
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
        self.label.setText(_translate("addwindow", "<html><head/><body><p><img src=\":/login/Pics/Login-window.png\"width=522 height=520/></p></body></html>"))
        self.idbox.setPlaceholderText(_translate("addwindow", "Enter ID"))
        self.tinbox.setPlaceholderText(_translate("addwindow", "Enter Time In"))
        self.toutbox.setPlaceholderText(_translate("addwindow", "Enter Time out"))
        self.daybox.setPlaceholderText(_translate("addwindow", "Enter Day"))
        self.sembox.setPlaceholderText(_translate("addwindow", "Enter Semester"))
        self.aybox.setPlaceholderText(_translate("addwindow", "Enter School Year"))        
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

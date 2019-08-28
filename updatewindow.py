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
        fname = self.fnamebox.text()
        lname = self.lnamebox.text()
        posbox = self.posbox.text()
        cbox = self.cbox.text()
        selected_account = [fname, lname, cbox, posbox, self.cell_student_number]
        query = "UPDATE stafferinfo SET first_name=\"{0}\", last_name=\"{1}\", program=\"{2}\", position=\"{3}\" WHERE student_number = \"{4}\"".format(*selected_account)
        QMessageBox.about(self, "Updated", "Updated!")
        cur.execute(query)
        conn.commit()
    def setupUi(self, updatewindow):
        self.updatewindow = updatewindow
        updatewindow.setObjectName("updatewindow")
        updatewindow.resize(329, 210)
        updatewindow.setMinimumSize(QtCore.QSize(329, 210))
        updatewindow.setMaximumSize(QtCore.QSize(329, 210))
        updatewindow.setStyleSheet("background-color: rgb(39, 39, 39);")
        self.centralwidget = QtWidgets.QWidget(updatewindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.clicked.connect(self.updateData)
        self.pushButton.setGeometry(QtCore.QRect(120, 160, 75, 23))
        self.pushButton.setStyleSheet("background-color: rgb(226, 226, 226);")
        self.pushButton.setObjectName("pushButton")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 40, 301, 31))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setStyleSheet("font: 14pt \"Bebas\";\n"
"color: rgb(255, 255, 0);")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.fnamebox = QtWidgets.QLineEdit(self.layoutWidget)
        self.fnamebox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.fnamebox.setObjectName("fnamebox")
        self.horizontalLayout.addWidget(self.fnamebox)
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 10, 301, 31))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_2.setStyleSheet("font: 14pt \"Bebas\";\n"
"color: rgb(255, 255, 0);")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.idbox = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.idbox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.idbox.setObjectName("idbox")
        self.horizontalLayout_2.addWidget(self.idbox)
        self.layoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_3.setGeometry(QtCore.QRect(10, 130, 301, 31))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_3.setStyleSheet("font: 14pt \"Bebas\";\n"
"color: rgb(255, 255, 0);")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.posbox = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.posbox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.posbox.setObjectName("posbox")
        self.horizontalLayout_3.addWidget(self.posbox)
        self.layoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_4.setGeometry(QtCore.QRect(10, 70, 301, 31))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_ = QtWidgets.QLabel(self.layoutWidget_4)
        self.label_.setStyleSheet("font: 14pt \"Bebas\";\n"
"color: rgb(255, 255, 0);")
        self.label_.setObjectName("label_")
        self.horizontalLayout_4.addWidget(self.label_)
        self.lnamebox = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.lnamebox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lnamebox.setObjectName("lnamebox")
        self.horizontalLayout_4.addWidget(self.lnamebox)
        self.layoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_5.setGeometry(QtCore.QRect(10, 100, 301, 31))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget_5)
        self.label_5.setStyleSheet("font: 14pt \"Bebas\";\n"
"color: rgb(255, 255, 0);")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.cbox = QtWidgets.QLineEdit(self.layoutWidget_5)
        self.cbox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cbox.setObjectName("cbox")
        self.horizontalLayout_5.addWidget(self.cbox)
        self.pushButton.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget_2.raise_()
        self.layoutWidget_3.raise_()
        self.layoutWidget_4.raise_()
        self.layoutWidget_5.raise_()
        self.label_5.raise_()
        updatewindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(updatewindow)
        self.statusbar.setObjectName("statusbar")
        updatewindow.setStatusBar(self.statusbar)

        self.retranslateUi(updatewindow)
        QtCore.QMetaObject.connectSlotsByName(updatewindow)

    def retranslateUi(self, updatewindow):
        _translate = QtCore.QCoreApplication.translate
        updatewindow.setWindowTitle(_translate("updatewindow", "MainWindow"))
        self.pushButton.setText(_translate("updatewindow", "Confirm"))
        self.label.setText(_translate("updatewindow", "first Name:"))
        self.label_2.setText(_translate("updatewindow", "Student ID: "))
        self.label_3.setText(_translate("updatewindow", "Position:          "))
        self.label_.setText(_translate("updatewindow", "Last Name:  "))
        self.label_5.setText(_translate("updatewindow", "Course:               "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    updatewindow = QtWidgets.QMainWindow()
    ui = Ui_updatewindow()
    ui.setupUi(updatewindow)
    updatewindow.show()
    sys.exit(app.exec_())
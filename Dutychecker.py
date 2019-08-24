from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox
import pymysql
from Login import Ui_adminlogin

class Ui_DutyChecker(QMainWindow):
    def login(self):
        conn = pymysql.connect('localhost', 'tipvoice', 'password', 'staffer')
        student_number=self.idbox.text()
        #first_name=self.namebox.text()
            #last_name=self.lineEdit_3.text()
            #position=self.lineEdit_4.text()
        with conn:
            cur=conn.cursor()
            query=("SELECT*FROM stafferinfo where student_number=%s")
            data=cur.execute(query,(student_number))
            if (cur.fetchall()):
                QMessageBox.about(self, 'Login', 'You successfully Logged In')
            elif(student_number==""):
                QMessageBox.about(self, 'Warning!', 'Please input student number.')
            else:
                QMessageBox.about(self, 'Warning!', "Staffer doesn't exist")
                
    def adminwindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_adminlogin()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, DutyChecker):
        DutyChecker.setObjectName("DutyChecker")
        DutyChecker.setEnabled(True)
        DutyChecker.resize(800, 450)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DutyChecker.sizePolicy().hasHeightForWidth())
        DutyChecker.setSizePolicy(sizePolicy)
        DutyChecker.setMinimumSize(QtCore.QSize(800, 450))
        DutyChecker.setMaximumSize(QtCore.QSize(800, 450))
        DutyChecker.setStyleSheet("background-color: rgb(26, 26, 26);")
        self.centralwidget = QtWidgets.QWidget(DutyChecker)
        self.centralwidget.setObjectName("centralwidget")
        self.Logo = QtWidgets.QLabel(self.centralwidget)
        self.Logo.setGeometry(QtCore.QRect(270, 10, 271, 121))
        self.Logo.setStyleSheet("image: url('Pics/Voice-logo.png')")
        self.Logo.setText("")
        self.logo.setSizePolicy("Fixed","Fixed",0,0)
        self.Logo.setObjectName("Logo")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 120, 251, 81))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(26, 26, 26))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(26, 26, 26))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(26, 26, 26))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(26, 26, 26))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(26, 26, 26))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(26, 26, 26))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(26, 26, 26))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(26, 26, 26))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(26, 26, 26))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Gobold Lowplus")
        font.setPointSize(49)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setObjectName("label")
        self.name = QtWidgets.QLabel(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(140, 190, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(36)
        self.name.setFont(font)
        self.name.setObjectName("name")
        self.Course = QtWidgets.QLabel(self.centralwidget)
        self.Course.setGeometry(QtCore.QRect(120, 240, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(36)
        self.Course.setFont(font)
        self.Course.setObjectName("Course")
        self.idbox = QtWidgets.QLineEdit(self.centralwidget)
        self.idbox.setGeometry(QtCore.QRect(300, 350, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.idbox.setFont(font)
        self.idbox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 18pt \"Bebas Neue\";")
        self.idbox.setObjectName("idbox")
        self.studid = QtWidgets.QLabel(self.centralwidget)
        self.studid.setGeometry(QtCore.QRect(110, 350, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(36)
        self.studid.setFont(font)
        self.studid.setStyleSheet("")
        self.studid.setObjectName("studid")
        self.position = QtWidgets.QLabel(self.centralwidget)
        self.position.setGeometry(QtCore.QRect(110, 290, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(36)
        self.position.setFont(font)
        self.position.setObjectName("position")
        self.namebox = QtWidgets.QLineEdit(self.centralwidget)
        self.namebox.setGeometry(QtCore.QRect(210, 200, 441, 31))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.namebox.setFont(font)
        self.namebox.setAutoFillBackground(False)
        self.namebox.setReadOnly(True)
        self.namebox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 18pt \"Bebas Neue\";")
        self.namebox.setText("")
        self.namebox.setObjectName("namebox")
        self.coursebox = QtWidgets.QLineEdit(self.centralwidget)
        self.coursebox.setGeometry(QtCore.QRect(210, 250, 441, 31))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.coursebox.setFont(font)
        self.coursebox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 18pt \"Bebas Neue\";")
        self.coursebox.setObjectName("coursebox")
        self.coursebox.setReadOnly(True)
        self.positionbox = QtWidgets.QLineEdit(self.centralwidget)
        self.positionbox.setGeometry(QtCore.QRect(210, 300, 441, 31))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.positionbox.setFont(font)
        self.positionbox.setReadOnly(True)
        self.positionbox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 18pt \"Bebas Neue\";")
        self.positionbox.setObjectName("positionbox")
        self.Time = QtWidgets.QLabel(self.centralwidget)
        self.Time.setGeometry(QtCore.QRect(790, 470, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(36)
        self.Time.setFont(font)
        self.Time.setObjectName("Time")
        self.date = QtWidgets.QLabel(self.centralwidget)
        self.date.setGeometry(QtCore.QRect(790, 520, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(36)
        self.date.setFont(font)
        self.date.setObjectName("date")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(310, 380, 239, 37))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.loginbut = QtWidgets.QPushButton(self.layoutWidget)
        self.loginbut.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.loginbut.setObjectName("loginbut")
        self.loginbut.clicked.connect(self.login)
        self.horizontalLayout.addWidget(self.loginbut)
        self.logoutbut = QtWidgets.QPushButton(self.layoutWidget)
        self.logoutbut.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.logoutbut.setObjectName("logoutbut")
        self.horizontalLayout.addWidget(self.logoutbut)
        self.adminbut = QtWidgets.QPushButton(self.layoutWidget)
        self.adminbut.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.adminbut.setObjectName("adminbut")
        self.adminbut.clicked.connect(self.adminwindow)
        self.horizontalLayout.addWidget(self.adminbut)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(590, 350, 56, 84))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.time = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(36)
        self.time.setFont(font)
        self.time.setStyleSheet("")
        self.time.setObjectName("time")
        self.verticalLayout.addWidget(self.time)
        self.date_2 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(36)
        self.date_2.setFont(font)
        self.date_2.setStyleSheet("")
        self.date_2.setObjectName("date_2")
        self.verticalLayout.addWidget(self.date_2)
        self.layoutWidget.raise_()
        self.Logo.raise_()
        self.label.raise_()
        self.name.raise_()
        self.Course.raise_()
        self.idbox.raise_()
        self.studid.raise_()
        self.position.raise_()
        self.namebox.raise_()
        self.coursebox.raise_()
        self.positionbox.raise_()
        self.Time.raise_()
        self.date.raise_()
        self.layoutWidget.raise_()
        DutyChecker.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(DutyChecker)
        self.statusbar.setObjectName("statusbar")
        DutyChecker.setStatusBar(self.statusbar)

        self.retranslateUi(DutyChecker)
        QtCore.QMetaObject.connectSlotsByName(DutyChecker)

    def retranslateUi(self, DutyChecker):
        _translate = QtCore.QCoreApplication.translate
        DutyChecker.setWindowTitle(_translate("DutyChecker", "MainWindow"))
        self.label.setText(_translate("DutyChecker", "<html><head/><body><p><span style=\" color:#ffff00;\">TIP VOICE</span></p></body></html>"))
        self.name.setText(_translate("DutyChecker", "<html><head/><body><p><span style=\" font-size:24pt; color:#ffff00;\">Name:</span></p></body></html>"))
        self.Course.setText(_translate("DutyChecker", "<html><head/><body><p><span style=\" font-size:24pt; color:#ffff00;\">Course:</span></p></body></html>"))
        self.idbox.setToolTip(_translate("DutyChecker", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Bebas Neue\'; font-size:36pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">sadsad</span></p></body></html>"))
        self.idbox.setPlaceholderText(_translate("DutyChecker", "Required field"))
        self.studid.setText(_translate("DutyChecker", "<html><head/><body><p><span style=\" font-size:24pt; color:#ffff00;\">Enter Student ID:</span></p></body></html>"))
        self.position.setText(_translate("DutyChecker", "<html><head/><body><p><span style=\" font-size:24pt; color:#ffff00;\">Position:</span></p></body></html>"))
        self.namebox.setToolTip(_translate("DutyChecker", "<html><head/><body><p><span style=\" font-size:12pt;\">rfdasd</span></p></body></html>"))
        self.Time.setText(_translate("DutyChecker", "<html><head/><body><p><span style=\" font-size:20pt; color:#ffff00;\">Time:</span></p></body></html>"))
        self.date.setText(_translate("DutyChecker", "<html><head/><body><p><span style=\" font-size:20pt; color:#ffff00;\">Date:</span></p></body></html>"))
        self.loginbut.setText(_translate("DutyChecker", "Login"))
        self.logoutbut.setText(_translate("DutyChecker", "Logout"))
        self.adminbut.setText(_translate("DutyChecker", "Admin"))
        self.time.setText(_translate("DutyChecker", "<html><head/><body><p><span style=\" font-size:24pt; color:#ffff00;\">Time:</span></p></body></html>"))
        self.date_2.setText(_translate("DutyChecker", "<html><head/><body><p><span style=\" font-size:24pt; color:#ffff00;\">date:</span></p></body></html>"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DutyChecker = QtWidgets.QMainWindow()
    ui = Ui_DutyChecker()
    ui.setupUi(DutyChecker)
    DutyChecker.show()
    sys.exit(app.exec_())

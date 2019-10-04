from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox
import pymysql
from newadminwindow import Ui_MainWindow


class Ui_adminlogin(QMainWindow):

    def addAdmin(self):
        conn = pymysql.connect('localhost', 'tipvoice', 'password', 'staffer')
        username=self.usernamebox.text()
        password=self.Password.text()
        with conn:
            cur=conn.cursor()
            query=("SELECT username, password FROM adminlogin")
            cur.execute(query)
            result = tuple(cur.fetchall()) # EXAMPLE OUTPUT: (('zeusjames', '12345'), ('ironman', '3000'))
            accounts = {}
            for account_number in range(0, len(result)):
                    accounts[result[account_number][0]] = result[account_number]
            if (username in accounts and password == accounts[username][1]):
                    QMessageBox.about(self, 'Warning', 'Admin already exists')
            elif (username=='' and password==''):
                    QMessageBox.about(self, 'Warning!', "Please input username/password!")
            else: 
                cur.execute("INSERT INTO adminlogin (username,password)" "values('%s','%s')" % (''.join(username), ''.join(password)))
                QMessageBox.about(self, 'Add Admin!', "Successfully added!")
                conn.commit()
                self.close()

    def admin(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        #self.window_ui.show() # .show() shows the self.admin_ui window
        self.this_window.hide()
        
    def loginadmin(self):
            conn = pymysql.connect('localhost', 'tipvoice', 'password', 'staffer')
            username=self.usernamebox.text()
            password=self.Password.text()
            with conn:
            # Let's say you already have values in the adminlogin table
            #
            # Example values:
            #
            #  ------------------------------
            #  |         adminlogin         |      <-- TABLE NAME
            #  ------------------------------
            #  |  username    |   password  |      <-- COLUMNS
            #  ------------------------------
            #  |  zeusjames   |   12345     |      <-- FIRST ROW
            #  |  iron man    |   3000      |      <-- SECOND ROW
            #  ------------------------------
            #
                cur=conn.cursor()
                query=("SELECT username, password FROM adminlogin")
                cur.execute(query)
                result = tuple(cur.fetchall()) # EXAMPLE OUTPUT: (('zeusjames', '12345'), ('ironman', '3000'))
                accounts = {} # Holds accounts as a dictionary

            # This for-loop statement organizes the values obtained by the "result" and pass it to "accounts"
            # To make the dictionary understandable, this is the output {<username>: ('<username>':<password>)} or
            # accounts = {value: tuple(value, value)}
            # NOTE: tuple is just like a list () = []
            # Example Output: {'zeusjames': ('zeusjames', '12345'), 'ironman': ('ironman', '3000')}
                for account_number in range(0, len(result)):
                    accounts[result[account_number][0]] = result[account_number]
                # Example:
                #   result[0][0] is 'zeusjames'
                #   result[0] is ('zeusjames', '12345')
                #   accounts['zeusjames']  = ('zeusjames', '12345')
                
            # If the username is in accounts and password is in accounts[username][1], then proceed
            # Example condition: If "zeusjames" is in accounts and password is in accounts["zeusjames"][1], then proceed
                if (username in accounts and password == accounts[username][1]):
                    QMessageBox.about(self, 'Login', 'You successfully Logged In')
                    self.admin()
                elif (username=='' and password==''):
                    QMessageBox.about(self, 'Warning!', "Please input username/password!")
                else: 
                    QMessageBox.about(self, 'Warning!', "Incorrect!")

    #def keyevent(self,event):
        #if event.key() == QtCore.Ket.Key_Return:
          # self.Adminlogin.clicked.connect(self.loginadmin)
       # return None


    def setupUi(self, adminlogin):
        self.this_window = adminlogin
        adminlogin.setObjectName("adminlogin")
        adminlogin.resize(606, 617)
        adminlogin.setStyleSheet("background:transparent;")
        adminlogin.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        adminlogin.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.centralwidget = QtWidgets.QWidget(adminlogin)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 60, 511, 481))
        self.label.setObjectName("label")

              
        self.usernamebox = QtWidgets.QLineEdit(self.centralwidget)
        self.usernamebox.setGeometry(QtCore.QRect(180, 290, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Nexa Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.usernamebox.setFont(font)
        self.usernamebox.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.usernamebox.setAlignment(QtCore.Qt.AlignCenter)
        self.usernamebox.setObjectName("usernamebox")
        self.usernamebox.setStyleSheet("Background:White")

        self.Password = QtWidgets.QLineEdit(self.centralwidget)
        self.Password.setGeometry(QtCore.QRect(180, 350, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Nexa Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Password.setFont(font)
        self.Password.setInputMask("")
        self.Password.setText("")
        self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password.setAlignment(QtCore.Qt.AlignCenter)
        self.Password.setObjectName("Password")
        self.Password.setStyleSheet("Background:White")

        self.Adminlogin = QtWidgets.QPushButton(self.centralwidget)
        self.Adminlogin.setGeometry(QtCore.QRect(220, 400, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Nexa Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Adminlogin.setFont(font)
        self.Adminlogin.setStyleSheet("QPushButton {background-color: Black} QPushButton:hover {background-color:grey}QPushButton {border-radius:15px}QPushButton {color:White}QPushButton{border:2px solid yellow}QPushButton:pressed{Background-color:yellow};")
        self.Adminlogin.setObjectName("Adminlogin")
        self.Adminlogin.clicked.connect(self.loginadmin)

        self.Signup = QtWidgets.QPushButton(self.centralwidget)
        self.Signup.setGeometry(QtCore.QRect(320, 400, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Nexa Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Signup.setFont(font)
        self.Signup.setStyleSheet("QPushButton {background-color: Black} QPushButton:hover {background-color:grey}QPushButton {border-radius:15px}QPushButton {color:White}QPushButton{border:2px solid yellow}QPushButton:pressed{Background-color:yellow};")
        self.Signup.setObjectName("Signup")
        self.Signup.clicked.connect(self.addAdmin)

        self.Exit = QtWidgets.QPushButton(self.centralwidget)
        self.Exit.setGeometry(QtCore.QRect(270, 440, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Nexa Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Exit.setFont(font)
        self.Exit.setStyleSheet("QPushButton {background-color: Black} QPushButton:hover {background-color:grey}QPushButton {border-radius:15px}QPushButton {color:White}QPushButton{border:2px solid yellow}QPushButton:pressed{Background-color:red};")
        self.Exit.setObjectName("Exit")
        self.Exit.clicked.connect(QtCore.QCoreApplication.instance().quit)

        adminlogin.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(adminlogin)
        self.statusbar.setObjectName("statusbar")
        adminlogin.setStatusBar(self.statusbar)

        adminlogin.keyPressEvent = self.defineKeyPressEvent

        self.retranslateUi(adminlogin)
        QtCore.QMetaObject.connectSlotsByName(adminlogin)

    def defineKeyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Return:
            self.loginadmin()
        if e.key() == QtCore.Qt.Key_Enter:
            self.loginadmin()

    def retranslateUi(self, adminlogin):
        _translate = QtCore.QCoreApplication.translate
        adminlogin.setWindowTitle(_translate("adminlogin", "MainWindow"))
        self.label.setText(_translate("adminlogin", "<html><head/><body><p><img src=\":/login/Pics/Login-window.png\"width=522 height=484/></p></body></html>"))
        self.Adminlogin.setText(_translate("adminlogin", "LOGIN"))
        self.Password.setPlaceholderText(_translate("adminlogin", "Enter Password"))
        self.usernamebox.setPlaceholderText(_translate("adminlogin", "Enter Username"))
        self.Signup.setText(_translate("adminlogin", "SIGNUP"))
        self.Exit.setText(_translate("adminlogin", "EXIT"))
import dutycheckerFiles_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Newmainwindow = QtWidgets.QMainWindow()
    ui = Ui_adminlogin()
    ui.setupUi(Newmainwindow)
    Newmainwindow.show()
    sys.exit(app.exec_())

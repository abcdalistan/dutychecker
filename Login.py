from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox
import pymysql
from adminwindow import Ui_MainWindow

class Ui_adminlogin(QMainWindow):
    def addAdmin(self):
        conn = pymysql.connect('localhost', 'tipvoice', 'password', 'staffer')
        username=self.usernamebox.text()
        password=self.lineEdit_2.text()
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
            password=self.lineEdit_2.text()
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

    def setupUi(self, adminlogin):
        self.this_window = adminlogin
        adminlogin.setObjectName("adminlogin")
        adminlogin.resize(422, 384)
        adminlogin.setMinimumSize(QtCore.QSize(422, 384))
        adminlogin.setMaximumSize(QtCore.QSize(422, 384))
        self.centralwidget = QtWidgets.QWidget(adminlogin)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(422, 364))
        self.centralwidget.setMaximumSize(QtCore.QSize(422, 364))
        self.centralwidget.setBaseSize(QtCore.QSize(422, 364))
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setEnabled(True)
        self.frame.setGeometry(QtCore.QRect(0, 0, 421, 381))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(421, 381))
        self.frame.setMaximumSize(QtCore.QSize(421, 381))
        self.frame.setStyleSheet("background-color:rgb(43, 43, 43);")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(80, 170, 271, 61))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Password = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Password.setFont(font)
        self.Password.setStyleSheet("font: 18pt \"Bebas Neue\";\n"
"color: rgb(255, 255, 0);")
        self.Password.setObjectName("Password")
        self.horizontalLayout_2.addWidget(self.Password)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.layoutWidget1 = QtWidgets.QWidget(self.frame)
        self.layoutWidget1.setGeometry(QtCore.QRect(80, 110, 271, 62))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Username = QtWidgets.QLabel(self.layoutWidget1)
        
        font = QtGui.QFont()
        font.setFamily("Bebas Neue")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Username.setFont(font)
        self.Username.setStyleSheet("font: 18pt \"Bebas Neue\";\n"
"color: rgb(255, 255, 0);")
        self.Username.setObjectName("Username")
        self.horizontalLayout.addWidget(self.Username)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.usernamebox = QtWidgets.QLineEdit(self.layoutWidget1)
        self.usernamebox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.usernamebox.setObjectName("usernamebox")
        self.verticalLayout.addWidget(self.usernamebox)
        self.layoutWidget2 = QtWidgets.QWidget(self.frame)
        self.layoutWidget2.setGeometry(QtCore.QRect(130, 240, 158, 25))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Adminlogin = QtWidgets.QPushButton(self.layoutWidget2)
        self.Adminlogin.setStyleSheet("background-color: rgb(195, 195, 195);")
        self.Adminlogin.setObjectName("Adminlogin")
        self.Adminlogin.clicked.connect(self.loginadmin)
        self.horizontalLayout_3.addWidget(self.Adminlogin)
        self.Signup = QtWidgets.QPushButton(self.layoutWidget2)
        self.Signup.setStyleSheet("background-color: rgb(195, 195, 195);")
        self.Signup.setObjectName("Signup")
        self.Signup.clicked.connect(self.addAdmin)
        self.horizontalLayout_3.addWidget(self.Signup)
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        adminlogin.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(adminlogin)
        self.statusbar.setObjectName("statusbar")
        adminlogin.setStatusBar(self.statusbar)

        self.retranslateUi(adminlogin)
        QtCore.QMetaObject.connectSlotsByName(adminlogin)

    def retranslateUi(self, adminlogin):
        _translate = QtCore.QCoreApplication.translate
        adminlogin.setWindowTitle(_translate("adminlogin", "MainWindow"))
        self.Password.setText(_translate("adminlogin", "Password:"))
        self.Username.setText(_translate("adminlogin", "USERname:"))
        self.Adminlogin.setText(_translate("adminlogin", "Login"))
        self.Signup.setText(_translate("adminlogin", "Sign up"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DutyChecker = QtWidgets.QMainWindow()
    ui = Ui_adminlogin()
    ui.setupUi(DutyChecker)
    DutyChecker.show()
    sys.exit(app.exec_())

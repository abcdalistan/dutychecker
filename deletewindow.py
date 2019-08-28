from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox
import pymysql

class Ui_deletewindow(QMainWindow):
    def deleteStaffer(self):
        conn = pymysql.connect('localhost', 'tipvoice', 'password', 'staffer')
        name=self.delnamebox.text()
        with conn:
            cur = conn.cursor()
            query = "SELECT * FROM stafferinfo;"
            cur.execute(query)
            result = tuple(cur.fetchall())
            accounts = {}
            for account_number in range(0, len(result)):
                accounts[result[account_number][0]] = result[account_number]
            if (name in accounts):
                query = "DELETE FROM stafferinfo where last_name= \"{}\"".format(name)
                cur.execute(query)
               # result = cur.fetchone()
                QMessageBox.about(self, 'Delete', 'Successfully deleted the staffer!')
            elif (name==""):
                QMessageBox.about(self, 'Warning!', "Please input name!")
            else:
                QMessageBox.about(self, 'Warning!', "Staffer doesn't exist!")
                conn.commit()

    def setupUi(self, deletewindow):
        deletewindow.setObjectName("deletewindow")
        deletewindow.resize(345, 110)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(deletewindow.sizePolicy().hasHeightForWidth())
        deletewindow.setSizePolicy(sizePolicy)
        deletewindow.setMinimumSize(QtCore.QSize(345, 110))
        deletewindow.setMaximumSize(QtCore.QSize(345, 110))
        deletewindow.setStyleSheet("background-color: rgb(43, 43, 43);")
        self.centralwidget = QtWidgets.QWidget(deletewindow)
        self.centralwidget.setObjectName("centralwidget")
        self.delconfirm = QtWidgets.QPushButton(self.centralwidget)
        self.delconfirm.setGeometry(QtCore.QRect(130, 70, 75, 23))
        self.delconfirm.setStyleSheet("background-color: rgb(225, 225, 225);")
        self.delconfirm.setObjectName("delconfirm")
        self.delconfirm.clicked.connect(self.deleteStaffer)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 20, 321, 41))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.delname = QtWidgets.QLabel(self.widget)
        self.delname.setStyleSheet("color: rgb(255, 255, 0);\n"
"font: 16pt \"Bebas\";")
        self.delname.setObjectName("delname")
        self.horizontalLayout.addWidget(self.delname)
        self.delnamebox = QtWidgets.QLineEdit(self.widget)
        self.delnamebox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.delnamebox.setObjectName("delnamebox")
        self.horizontalLayout.addWidget(self.delnamebox)
        deletewindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(deletewindow)
        self.statusbar.setObjectName("statusbar")
        deletewindow.setStatusBar(self.statusbar)

        self.retranslateUi(deletewindow)
        QtCore.QMetaObject.connectSlotsByName(deletewindow)

    def retranslateUi(self, deletewindow):
        _translate = QtCore.QCoreApplication.translate
        deletewindow.setWindowTitle(_translate("deletewindow", "MainWindow"))
        self.delconfirm.setText(_translate("deletewindow", "Confirm"))
        self.delname.setText(_translate("deletewindow", "Name:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    deletewindow = QtWidgets.QMainWindow()
    ui = Ui_deletewindow()
    ui.setupUi(deletewindow)
    deletewindow.show()
    sys.exit(app.exec_())

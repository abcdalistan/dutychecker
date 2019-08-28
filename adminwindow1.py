from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox
import pymysql
from addwindow import Ui_addwindow
from deletewindow import Ui_deletewindow
from searchwindow import Ui_searchwindow

class Ui_MainWindow(QMainWindow):
    def cell_was_clicked(self, row, column):
        #print("Row %d and Column %d was clicked" % (row, column))
        item = self.tableWidget.item(row, column)
        print(row+1)

    def addTable(self,columns):
        rowPosition=self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowPosition)

        for i, column in enumerate(columns):
            self.tableWidget.setItem(rowPosition,i, QtWidgets.QTableWidgetItem(str(column)))

    def viewDuty(self):
        conn = pymysql.connect('localhost', 'tipvoice', 'password', 'staffer')
        with conn:
            cur=conn.cursor()
            query=("SELECT * FROM stafferinfo")
            cur.execute(query)
            result = cur.fetchall()
            for row in result:
                self.addTable(row)
            cur.close()
            
    def addwindow(self):
        self.addwindow = QtWidgets.QMainWindow()
        self.ui = Ui_addwindow()
        self.ui.setupUi(self.addwindow)
        self.addwindow.show()

    def deletewindow(self):
        self.deletewindow = QtWidgets.QMainWindow()
        self.ui = Ui_deletewindow()
        self.ui.setupUi(self.deletewindow)
        self.deletewindow.show()

    def searchwindow(self):
        self.searchwindow = QtWidgets.QMainWindow()
        self.ui = Ui_searchwindow()
        self.ui.setupUi(self.searchwindow)
        self.searchwindow.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 450)
        MainWindow.setMinimumSize(QtCore.QSize(800, 450))
        MainWindow.setMaximumSize(QtCore.QSize(800, 450))
        MainWindow.setStyleSheet("background-color: rgb(29, 29, 29);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 40, 151, 391))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.daybox = QtWidgets.QComboBox(self.frame)
        self.daybox.setGeometry(QtCore.QRect(10, 10, 131, 21))
        self.daybox.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.daybox.setObjectName("daybox")
        self.daybox.addItem("")
        self.daybox.addItem("")
        self.daybox.addItem("")
        self.daybox.addItem("")
        self.daybox.addItem("")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)

        self.tableWidget.cellClicked.connect(self.cell_was_clicked)

        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QtCore.QRect(170, 40, 621, 391))
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.CustomDashLine)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(200)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 781, 27))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addbut = QtWidgets.QPushButton(self.widget)
        self.addbut.setStyleSheet("background-color: rgb(226, 226, 226);")
        self.addbut.setObjectName("addbut")
        self.addbut.clicked.connect(self.addwindow)
        self.horizontalLayout.addWidget(self.addbut)
        self.delbut = QtWidgets.QPushButton(self.widget)
        self.delbut.setStyleSheet("background-color: rgb(226, 226, 226);")
        self.delbut.setObjectName("delbut")
        self.delbut.clicked.connect(self.deletewindow)
        self.horizontalLayout.addWidget(self.delbut)
        self.searchbut = QtWidgets.QPushButton(self.widget)
        self.searchbut.setStyleSheet("background-color: rgb(226, 226, 226);")
        self.searchbut.setObjectName("searchbut")
        self.searchbut.clicked.connect(self.searchwindow)
        self.horizontalLayout.addWidget(self.searchbut)
        self.viewbut = QtWidgets.QPushButton(self.widget)
        self.viewbut.setStyleSheet("background-color: rgb(226, 226, 226);")
        self.viewbut.setObjectName("viewbut")
        self.horizontalLayout.addWidget(self.viewbut)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.updatebut = QtWidgets.QPushButton(self.widget)
        self.updatebut.setStyleSheet("background-color: rgb(226, 226, 226);")
        self.updatebut.setObjectName("updatebut")
        self.horizontalLayout_2.addWidget(self.updatebut)
        self.refreshbut = QtWidgets.QPushButton(self.widget)
        self.refreshbut.setStyleSheet("background-color: rgb(226, 226, 226);")
        self.refreshbut.setObjectName("refreshbut")
        self.horizontalLayout_2.addWidget(self.refreshbut)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.daybox.setCurrentText(_translate("MainWindow", "Monday"))
        self.daybox.setItemText(0, _translate("MainWindow", "Monday"))
        self.daybox.activated.connect(self.viewDuty)
        self.daybox.setItemText(1, _translate("MainWindow", "Tuesday"))
        self.daybox.setItemText(2, _translate("MainWindow", "Wednesday"))
        self.daybox.setItemText(3, _translate("MainWindow", "Thursday"))
        self.daybox.setItemText(4, _translate("MainWindow", "Friday"))
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Time"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name of Staffer"))
        self.addbut.setText(_translate("MainWindow", "Add"))
        self.delbut.setText(_translate("MainWindow", "Delete"))
        self.searchbut.setText(_translate("MainWindow", "Search"))
        self.viewbut.setText(_translate("MainWindow", "View"))
        self.updatebut.setText(_translate("MainWindow", "Update"))
        self.refreshbut.setText(_translate("MainWindow", "Refresh"))
import BG_rc
#import Icon_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

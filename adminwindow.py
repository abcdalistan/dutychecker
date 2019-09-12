
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox
import pymysql
from addwindow import Ui_addwindow
from searchwindow import Ui_searchwindow
from viewwindow import Ui_MainWindow as viewwindow
from updatewindow import Ui_updatewindow as updatewindow

class Ui_MainWindow(QMainWindow):
    def cell_was_clicked(self, row, column):
        self.row = row

    def addTable(self,columns):
        rowPosition=self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowPosition)
        for i, column in enumerate(columns):
            self.tableWidget.setItem(rowPosition,i, QtWidgets.QTableWidgetItem(str(column)))

    def viewStaffer(self):
        if self.flag:
            conn = pymysql.connect('localhost', 'tipvoice', 'password', 'staffer')
            with conn:
                cur=conn.cursor()
                query=("SELECT * FROM stafferinfo")
                cur.execute(query)
                result = cur.fetchall()
                for row in result:
                    self.addTable(row)
                cur.close()
            self.flag = 0
            #adding table when display button is clicked

    def refreshfunc(self):
        self.tableWidget.setRowCount(0)
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

    def searchWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_searchwindow()
        self.ui.setupUi(self.window)
        self.window.show()
        
    def viewwindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = viewwindow()
        self.ui.setupUi(self.window)
        self.window.show()

    # Don't mind about the decorator '@QtCore.pyqtSlot()'
    @QtCore.pyqtSlot()
    def deleteClicked(self):
        try:
            answer = QMessageBox.question(self, "", "Are you sure you want to delete student number '{0}'".format(self.tableWidget.item(self.row, 0).text()))
            if answer == QMessageBox.Yes:
                try:
                    conn = pymysql.connect("localhost", "tipvoice", "password", "staffer")
                    with conn:
                        cur = conn.cursor()
                        query = "DELETE FROM stafferinfo WHERE student_number = \'{0}\'".format(self.tableWidget.item(self.row, 0).text())
                        cur.execute(query)
                        conn.commit()
                        cur.close()
                    self.tableWidget.removeRow(self.row)
                    QMessageBox.about(self, "Delete", "Student number '{0}' has been deleted.".format(self.tableWidget.item(self.row, 0).text()))
                except:
                    pass
            else:
                return
        except:
            pass

    def openUpdateWindow(self):
        try:
            cell_student_number = self.tableWidget.item(self.row, 0).text()
            self.window = QtWidgets.QMainWindow()
            self.ui = updatewindow(self)
            self.ui.setupUi(self.window)
            self.ui.insertData(cell_student_number)
            self.window.show()
        except:
            pass
        else:
            return

    def setupUi(self, MainWindow):
        self.flag = 1
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 450)
        MainWindow.setMinimumSize(QtCore.QSize(800, 450))
        MainWindow.setMaximumSize(QtCore.QSize(800, 450))
        MainWindow.setStyleSheet("background-color: rgb(29, 29, 29);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.cellClicked.connect(self.cell_was_clicked)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QtCore.QRect(10, 40, 781, 391))
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.CustomDashLine)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(100)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 781, 27))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addbut = QtWidgets.QPushButton(self.layoutWidget)
        self.addbut.setStyleSheet("QPushButton {background-color: rgb(226, 226, 226)} QPushButton:hover {background-color: yellow};")
        self.addbut.setObjectName("addbut")
        self.addbut.clicked.connect(self.addwindow)
        self.horizontalLayout.addWidget(self.addbut)
        self.delbut = QtWidgets.QPushButton(self.layoutWidget)
        self.delbut.clicked.connect(self.deleteClicked) # <--------- DELETE BUTTON FUNCTION
        self.delbut.setStyleSheet("QPushButton {background-color: rgb(226, 226, 226)} QPushButton:hover {background-color: yellow};")
        self.delbut.setObjectName("delbut")
        self.horizontalLayout.addWidget(self.delbut)
        self.searchbut = QtWidgets.QPushButton(self.layoutWidget)
        self.searchbut.setStyleSheet("QPushButton {background-color: rgb(226, 226, 226)} QPushButton:hover {background-color: yellow};")
        self.searchbut.setObjectName("searchbut")
        self.searchbut.clicked.connect(self.searchWindow)
        self.horizontalLayout.addWidget(self.searchbut)
        self.viewbut = QtWidgets.QPushButton(self.layoutWidget)
        self.viewbut.setStyleSheet("QPushButton {background-color: rgb(226, 226, 226)} QPushButton:hover {background-color: yellow};")
        self.viewbut.setObjectName("viewbut")
        self.viewbut.clicked.connect(self.viewwindow)
        self.horizontalLayout.addWidget(self.viewbut)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.updatebut = QtWidgets.QPushButton(self.layoutWidget)
        self.updatebut.clicked.connect(self.openUpdateWindow)
        self.updatebut.setStyleSheet("QPushButton {background-color: rgb(226, 226, 226)} QPushButton:hover {background-color: yellow};")
        self.updatebut.setObjectName("updatebut")
        self.updatebut.clicked.connect(self.openUpdateWindow)
        self.horizontalLayout_2.addWidget(self.updatebut)
        self.refreshbut = QtWidgets.QPushButton(self.layoutWidget)
        self.refreshbut.setStyleSheet("QPushButton {background-color: rgb(226, 226, 226)} QPushButton:hover {background-color: yellow};")
        self.refreshbut.setObjectName("refreshbut")
        self.refreshbut.clicked.connect(self.refreshfunc)
        self.horizontalLayout_2.addWidget(self.refreshbut)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.viewStaffer()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Student no."))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Firstname"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Lastname"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Program"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Position"))
        self.addbut.setText(_translate("MainWindow", "Add"))
        self.delbut.setText(_translate("MainWindow", "Delete"))
        self.searchbut.setText(_translate("MainWindow", "Search"))
        self.viewbut.setText(_translate("MainWindow", "View"))
        self.updatebut.setText(_translate("MainWindow", "Update"))
        self.refreshbut.setText(_translate("MainWindow", "Refresh"))
        #self.displaybut.setText(_translate("MainWindow", "Display"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'viewwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 450)
        MainWindow.setMinimumSize(QtCore.QSize(800, 450))
        MainWindow.setMaximumSize(QtCore.QSize(800, 450))
        MainWindow.setStyleSheet("background-color: rgb(29, 29, 29);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.dutytable = QtWidgets.QTableWidget(self.centralwidget)
        self.dutytable.setEnabled(True)
        self.dutytable.setGeometry(QtCore.QRect(180, 10, 611, 421))
        self.dutytable.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dutytable.setFrameShape(QtWidgets.QFrame.Box)
        self.dutytable.setDragDropOverwriteMode(False)
        self.dutytable.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.dutytable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.dutytable.setShowGrid(True)
        self.dutytable.setGridStyle(QtCore.Qt.CustomDashLine)
        self.dutytable.setRowCount(0)
        self.dutytable.setColumnCount(2)
        self.dutytable.setObjectName("dutytable")
        item = QtWidgets.QTableWidgetItem()
        self.dutytable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.dutytable.setHorizontalHeaderItem(1, item)
        self.dutytable.horizontalHeader().setVisible(True)
        self.dutytable.horizontalHeader().setDefaultSectionSize(90)
        self.dutytable.horizontalHeader().setHighlightSections(True)
        self.dutytable.horizontalHeader().setMinimumSectionSize(100)
        self.dutytable.horizontalHeader().setSortIndicatorShown(False)
        self.dutytable.horizontalHeader().setStretchLastSection(True)
        self.dutytable.verticalHeader().setVisible(True)
        self.dutytable.verticalHeader().setCascadingSectionResizes(False)
        self.dutytable.verticalHeader().setDefaultSectionSize(30)
        self.dutytable.verticalHeader().setHighlightSections(True)
        self.dutytable.verticalHeader().setSortIndicatorShown(False)
        self.dutytable.verticalHeader().setStretchLastSection(False)
        self.viewwindow = QtWidgets.QFrame(self.centralwidget)
        self.viewwindow.setGeometry(QtCore.QRect(10, 10, 161, 421))
        self.viewwindow.setFrameShape(QtWidgets.QFrame.Box)
        self.viewwindow.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.viewwindow.setLineWidth(1)
        self.viewwindow.setObjectName("viewwindow")
        self.daybox = QtWidgets.QComboBox(self.viewwindow)
        self.daybox.setGeometry(QtCore.QRect(20, 40, 121, 22))
        self.daybox.setStyleSheet("background-color: rgb(225, 225, 225);")
        self.daybox.setObjectName("daybox")
        self.daybox.addItem("")
        self.daybox.addItem("")
        self.daybox.addItem("")
        self.daybox.addItem("")
        self.daybox.addItem("")
        self.editbut = QtWidgets.QPushButton(self.viewwindow)
        self.editbut.setGeometry(QtCore.QRect(40, 70, 75, 23))
        self.editbut.setStyleSheet("background-color: rgb(234, 234, 234);")
        self.editbut.setObjectName("editbut")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.dutytable.setSortingEnabled(False)
        item = self.dutytable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Time"))
        item = self.dutytable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name of Staffer"))
        self.daybox.setCurrentText(_translate("MainWindow", "Monday"))
        self.daybox.setItemText(0, _translate("MainWindow", "Monday"))
        self.daybox.setItemText(1, _translate("MainWindow", "Teusday"))
        self.daybox.setItemText(2, _translate("MainWindow", "Wednesday"))
        self.daybox.setItemText(3, _translate("MainWindow", "Thursday"))
        self.daybox.setItemText(4, _translate("MainWindow", "Friday"))
        self.editbut.setText(_translate("MainWindow", "Edit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

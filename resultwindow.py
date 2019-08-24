# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resultwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_resultwindow(object):
    def setupUi(self, resultwindow):
        resultwindow.setObjectName("resultwindow")
        resultwindow.resize(440, 270)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(resultwindow.sizePolicy().hasHeightForWidth())
        resultwindow.setSizePolicy(sizePolicy)
        resultwindow.setMinimumSize(QtCore.QSize(440, 270))
        resultwindow.setMaximumSize(QtCore.QSize(440, 270))
        resultwindow.setStyleSheet("background-color: rgb(38, 38, 38);")
        self.centralwidget = QtWidgets.QWidget(resultwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 10, 151, 31))
        self.label.setStyleSheet("font: 20pt \"Bebas\";\n"
"color: rgb(255, 255, 0);")
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 50, 421, 201))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.rname = QtWidgets.QLabel(self.widget)
        self.rname.setStyleSheet("font: 16pt \"Bebas\";\n"
"color: rgb(255, 255, 0);")
        self.rname.setObjectName("rname")
        self.horizontalLayout.addWidget(self.rname)
        self.rnamebox = QtWidgets.QLineEdit(self.widget)
        self.rnamebox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.rnamebox.setInputMask("")
        self.rnamebox.setReadOnly(True)
        self.rnamebox.setObjectName("rnamebox")
        self.horizontalLayout.addWidget(self.rnamebox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.rcourse = QtWidgets.QLabel(self.widget)
        self.rcourse.setStyleSheet("font: 16pt \"Bebas\";\n"
"color: rgb(255, 255, 0);")
        self.rcourse.setObjectName("rcourse")
        self.horizontalLayout_2.addWidget(self.rcourse)
        self.rcoursebox = QtWidgets.QLineEdit(self.widget)
        self.rcoursebox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.rcoursebox.setReadOnly(True)
        self.rcoursebox.setObjectName("rcoursebox")
        self.horizontalLayout_2.addWidget(self.rcoursebox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.rposition = QtWidgets.QLabel(self.widget)
        self.rposition.setStyleSheet("font: 16pt \"Bebas\";\n"
"color: rgb(255, 255, 0);")
        self.rposition.setObjectName("rposition")
        self.horizontalLayout_3.addWidget(self.rposition)
        self.rpositionbox = QtWidgets.QLineEdit(self.widget)
        self.rpositionbox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.rpositionbox.setReadOnly(True)
        self.rpositionbox.setObjectName("rpositionbox")
        self.horizontalLayout_3.addWidget(self.rpositionbox)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.rid = QtWidgets.QLabel(self.widget)
        self.rid.setStyleSheet("font: 16pt \"Bebas\";\n"
"color: rgb(255, 255, 0);")
        self.rid.setObjectName("rid")
        self.horizontalLayout_4.addWidget(self.rid)
        self.ridbox = QtWidgets.QLineEdit(self.widget)
        self.ridbox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ridbox.setReadOnly(True)
        self.ridbox.setObjectName("ridbox")
        self.horizontalLayout_4.addWidget(self.ridbox)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.rname.raise_()
        self.rcourse.raise_()
        self.rposition.raise_()
        self.rid.raise_()
        self.rnamebox.raise_()
        self.rcoursebox.raise_()
        self.rpositionbox.raise_()
        self.ridbox.raise_()
        self.rnamebox.raise_()
        self.label.raise_()
        resultwindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(resultwindow)
        self.statusbar.setObjectName("statusbar")
        resultwindow.setStatusBar(self.statusbar)

        self.retranslateUi(resultwindow)
        QtCore.QMetaObject.connectSlotsByName(resultwindow)

    def retranslateUi(self, resultwindow):
        _translate = QtCore.QCoreApplication.translate
        resultwindow.setWindowTitle(_translate("resultwindow", "MainWindow"))
        self.label.setText(_translate("resultwindow", "INFORMATION"))
        self.rname.setText(_translate("resultwindow", "Name:                       "))
        self.rcourse.setText(_translate("resultwindow", "Course:               "))
        self.rposition.setText(_translate("resultwindow", "Position:         "))
        self.rid.setText(_translate("resultwindow", "Student id:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    resultwindow = QtWidgets.QMainWindow()
    ui = Ui_resultwindow()
    ui.setupUi(resultwindow)
    resultwindow.show()
    sys.exit(app.exec_())

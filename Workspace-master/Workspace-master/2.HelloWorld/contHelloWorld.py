from PyQt5 import QtWidgets
import viewHelloWorld

class ContHelloWorld(QtWidgets.QDialog):
    def __init__(self, parent = None):
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = viewHelloWorld.Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.btnQuit.clicked.connect(self.close)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myform = ContHelloWorld()
    myform.show()
    sys.exit(app.exec_())
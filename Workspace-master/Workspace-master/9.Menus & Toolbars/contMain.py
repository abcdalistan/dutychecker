from PyQt5 import QtWidgets
import viewMain

class ContMain(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = viewMain.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.actionDelete.triggered.connect(self.actDelete)
        self.ui.actionNew.triggered.connect(self.actNew)
        self.ui.actionOpen.triggered.connect(self.actOpen)
        self.ui.actionSave.triggered.connect(self.actSave)

    def actDelete(self):
        QtWidgets.QMessageBox.information(self, "Delete", "Delete btn Pressed")

    def actNew(self):
        QtWidgets.QMessageBox.information(self, "New", "New btn Pressed")

    def actOpen(self):
        QtWidgets.QMessageBox.information(self, "Open", "Open btn Pressed")

    def actSave(self):
        QtWidgets.QMessageBox.information(self, "Save", "Save btn Pressed")



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    c = ContMain()
    c.show()
    sys.exit(app.exec_())
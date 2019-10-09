from PyQt5 import QtWidgets
import  viewListInput

class ContListInput(QtWidgets.QWidget):
    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = viewListInput.Ui_Form()
        self.ui.setupUi(self)

        self.ui.btnAdd.clicked.connect(self.add)
        self.ui.btnEdit.clicked.connect(self.edit)
        self.ui.btnDelete.clicked.connect(self.delete)
        self.ui.btnDeleteAll.clicked.connect(self.deleteAll)

    def add(self):
        self.ui.listWidget.addItem(self.ui.txtText.text())

    def edit(self):
        self.row = self.ui.listWidget.currentRow()
        self.msg, self.ok = QtWidgets.QInputDialog.getText(self, "Input", "Please enter a value")

        if self.ok:
            self.ui.listWidget.takeItem(self.row)
            self.ui.listWidget.insertItem(self.row, self.msg)

    def delete(self):
        self.row = self.ui.listWidget.currentRow()
        self.ui.listWidget.takeItem(self.row)

    def deleteAll(self):
        self.ui.listWidget.clear()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    c = ContListInput()
    c.show()
    sys.exit(app.exec_())
from PyQt5 import QtWidgets
import viewTable

class ContTable(QtWidgets.QWidget):
    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = viewTable.Ui_Form()
        self.ui.setupUi(self)

        self.dataList = []
        self.dataList.append(['Peter', 'Pan','12312'])
        self.dataList.append(['Pac', 'Man', '010001'])
        self.dataList.append(['Bilbo', 'Bagens', '42342'])
        self.dataList.append(['Han', 'Solo', '007'])

        for row in (self.dataList):
            self.ui.tableWidget.insertRow(0)

        for col in (self.dataList[0]):
            self.ui.tableWidget.insertColumn(0)

        for rowNr, rowValue in enumerate(self.dataList):
            for itemNr, itemValue in enumerate(rowValue):
                print(rowNr, itemNr, self.dataList[rowNr][itemNr])
                self.ui.tableWidget.setItem(rowNr, itemNr, QtWidgets.QTableWidgetItem(self.dataList[rowNr][itemNr]))

        self.ui.btnDelete.clicked.connect(self.delete)
        self.ui.btnAdd.clicked.connect(self.add)

    def delete(self):
        self.ui.tableWidget.removeRow(self.ui.tableWidget.currentRow())

    def add(self):
        self.ui.tableWidget.insertRow(self.ui.tableWidget.rowCount())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    c = ContTable()
    c.show()
    sys.exit(app.exec_())
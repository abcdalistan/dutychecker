from PyQt5 import QtWidgets
import viewRadChk

class ContRadChk(QtWidgets.QWidget):
    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self, parent)

        self.ui = viewRadChk.Ui_Form()
        self.ui.setupUi(self)

        self.ui.radLarge.clicked.connect(self.calculate)
        self.ui.radMed.clicked.connect(self.calculate)
        self.ui.radSmall.clicked.connect(self.calculate)

        self.ui.chkChips.clicked.connect(self.calculate)
        self.ui.chkCooldrink.clicked.connect(self.calculate)

        self.ui.spinbox.editingFinished.connect(self.calculate)

    def calculate(self):
        total = 0
        if self.ui.radLarge.isChecked():
            total += 6
        elif self.ui.radMed.isChecked():
            total += 5
        elif self.ui.radSmall.isChecked():
            total += 4

        if self.ui.chkChips.isChecked():
            total += 4

        if self.ui.chkCooldrink.isChecked():
            total += 5

        total = total * self.ui.spinbox.value()

        self.ui.lblTotal.setText("$ " + str(total))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    c = ContRadChk()
    c.show()
    sys.exit(app.exec_())

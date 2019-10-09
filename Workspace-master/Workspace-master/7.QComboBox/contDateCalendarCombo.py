from PyQt5 import QtWidgets
import viewDateCalendarCombo

class ContDateCalendar(QtWidgets.QWidget):
    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = viewDateCalendarCombo.Ui_Form()
        self.ui.setupUi(self)

        self.classList = ['First', 'Second', 'Bussiness', 'Economic']
        for i in self.classList:
            self.ui.cmbClass.addItem(i)

        self.ui.btnCalc.clicked.connect(self.calc)


    def calc(self):
        self.ui.lblSummery.setText("Summery: " + self.ui.calendarWidget.selectedDate().toString() + ", " + \
                                   str(self.ui.spnPersons.value()) + ", " + \
                                   self.ui.cmbClass.itemText(self.ui.cmbClass.currentIndex()))

        self.ticketCost = 0
        if self.ui.cmbClass.currentIndex() == 0:
            self.ticketCost = 100
        elif self.ui.cmbClass.currentIndex() == 1:
            self.ticketCost = 80
        elif self.ui.cmbClass.currentIndex() == 2:
            self.ticketCost = 70
        elif self.ui.cmbClass.currentIndex() == 3:
            self.ticketCost = 2
        print(self.ticketCost)

        self.ticketCost *= self.ui.spnPersons.value()
        print(self.ticketCost)

        self.ui.lblCost.setText("Ticket Cost: " + str(self.ticketCost))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    c = ContDateCalendar()
    c.show()
    sys.exit(app.exec_())
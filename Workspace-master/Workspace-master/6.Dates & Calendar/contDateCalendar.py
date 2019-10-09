from PyQt5 import QtWidgets
import viewDateCalendar

class ContDateCalendar(QtWidgets.QWidget):
    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = viewDateCalendar.Ui_Form()
        self.ui.setupUi(self)

        self.ui.calendarWidget.selectionChanged.connect(self.calDateChanged)
        self.ui.dateEdit.dateChanged.connect(self.dateEditChanged)

    def calDateChanged(self):
        self.ui.dateEdit.setDate(self.ui.calendarWidget.selectedDate())

    def dateEditChanged(self):
        self.ui.calendarWidget.setSelectedDate(self.ui.dateEdit.date())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    c = ContDateCalendar()
    c.show()
    sys.exit(app.exec_())
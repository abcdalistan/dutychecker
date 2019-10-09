from PyQt5 import QtWidgets, QtCore
import viewLCDClock

class ContLCDClock(QtWidgets.QWidget):
    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = viewLCDClock.Ui_Form()
        self.ui.setupUi(self)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updateLCD)
        self.timer.start(1000)

    def updateLCD(self):
        self.currentTime = QtCore.QTime.currentTime()
        self.strCurrentTime = self.currentTime.toString('hh:mm')
        self.ui.lcdNumber.display(self.strCurrentTime)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    c = ContLCDClock()
    c.show()
    sys.exit(app.exec_())
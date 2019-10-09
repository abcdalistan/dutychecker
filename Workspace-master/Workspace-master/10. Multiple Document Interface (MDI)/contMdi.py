from PyQt5 import QtWidgets
import viewMdi
import contLCDClock

class ContMdi(QtWidgets.QWidget):
    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = viewMdi.Ui_Form()
        self.ui.setupUi(self)

        self.subWin1 = QtWidgets.QMdiSubWindow()
        self.subWin2 = contLCDClock.ContLCDClock()
        self.subWin3 = QtWidgets.QMdiSubWindow()

        self.ui.mdiArea.addSubWindow(self.subWin1)
        self.ui.mdiArea.addSubWindow(self.subWin2)
        self.ui.mdiArea.addSubWindow(self.subWin3)

        self.ui.btnNext.clicked.connect(self.next)
        self.ui.btnPrev.clicked.connect(self.prev)
        self.ui.btnCloseAll.clicked.connect(self.closeAll)
        self.ui.btnCascade.clicked.connect(self.cascade)
        self.ui.btnTile.clicked.connect(self.tile)
        self.ui.btnSubWinView.clicked.connect(self.subWindow)
        self.ui.btnTabView.clicked.connect(self.tabView)

    def next(self):
        self.ui.mdiArea.activateNextSubWindow()

    def prev(self):
        self.ui.mdiArea.activatePreviousSubWindow()

    def closeAll(self):
        self.ui.mdiArea.closeAllSubWindows()

    def cascade(self):
        self.ui.mdiArea.cascadeSubWindows()

    def tile(self):
        self.ui.mdiArea.tileSubWindows()

    def subWindow(self):
        self.ui.mdiArea.setViewMode(0)
        self.ui.mdiArea.tileSubWindows()

    def tabView(self):
        self.ui.mdiArea.setViewMode(1)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    c = ContMdi()
    c.show()
    sys.exit(app.exec_())
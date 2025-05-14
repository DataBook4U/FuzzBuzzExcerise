#Desktop Application:
import sys
from PyQt6 import QtWidgets
from ui.mainwindow import Ui_MainWindow

app = QtWidgets.QApplication(sys.argv)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.setWindowTitle("FuzzBuzzAufgabe")

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #self.ui.ProgStart.clicked.connect(self.ui.)

window = MainWindow()



window.show()

sys.exit(app.exec())


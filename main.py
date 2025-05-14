#Desktop Application:
import sys
from PyQt6 import QtWidgets
from ui.mainwindow import Ui_MainWindow
from FuzzBuzz import Zahlenspiel

app = QtWidgets.QApplication(sys.argv)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.setWindowTitle("FuzzBuzzAufgabe")

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.ProgStart.clicked.connect(self.on_button_click)

    def on_button_click(self):
        s = self.ui.Startw.text()
        e = self.ui.Endw.text()
        aufgabe = Zahlenspiel(int(s), int(e))
        ergebnis = aufgabe.FuzzBuzzRätsel()
        self.ui.textBrowser.setText(ergebnis)

window = MainWindow()



window.show()

sys.exit(app.exec())


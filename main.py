#Desktop Application:
import sys
from PyQt6 import QtWidgets
from ui.mainwindow import Ui_MainWindow

app = QtWidgets.QApplication(sys.argv)

window = QtWidgets.QMainWindow()
window.setWindowTitle("FuzzBuzzAufgabe")

ui_window = Ui_MainWindow()
ui_window.setupUi(window)


window.show()


#FuzzBuzz Exercise:

class Zahlenspiel:
    def __init__(self, Startbereich, Endbereich):
        self.Startbereich = Startbereich
        self.Endbereich = Endbereich

    def FuzzBuzzRätsel(self):
        for i in range(self.Startbereich, self.Endbereich):
            if i % 3 == 0 and i % 5 == 0:
                print("FuzzBuzz")
            elif i % 3 == 0:
                print("Fuzz")
            elif i % 5 == 0:
                print("Buzz")
            else:
                print(i)

aufgabe = Zahlenspiel(1, 20)
aufgabe.FuzzBuzzRätsel()



sys.exit(app.exec())


#FuzzBuzz Exercise:

class Zahlenspiel:
    def __init__(self, Startbereich, Endbereich):
        self.Startbereich = Startbereich
        self.Endbereich = Endbereich

    def FuzzBuzzRätsel(self):
        ergebnis = ""
        for i in range(self.Startbereich, self.Endbereich + 1):
            if i % 3 == 0 and i % 5 == 0:
                ergebnis += "FuzzBuzz\n"
            elif i % 3 == 0:
                ergebnis += "Fuzz\n"
            elif i % 5 == 0:
                ergebnis += "Buzz\n"
            else:
                ergebnis += f"{i}\n"
        return ergebnis


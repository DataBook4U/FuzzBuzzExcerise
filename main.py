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
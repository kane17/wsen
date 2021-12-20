class Tier:
    def __init__(self, name, farbe, alter):
        self.name = name
        self.farbe = farbe
        self.alter = alter

    def schlafen(self, dauer):
        print(self.name+" schläft am Tag etwa "+dauer+" Stunden.")

    def reden(self, anzahl):
        print(self.name+" gibt kaum Laute von sich und immer unterschiedlich. Etwa jedoch "+anzahl+" pro Tag")

    def fressen(self, mahlzeit, anzahl):
        print(self.name+" isst ganz normales "+mahlzeit+". Dies etwa "+anzahl+" am Tag.")


    def _str_(self):
        self.schlafen("12")
        self.reden("4")
        self.fressen("Tierfutter", "3-4")


class Katze(Tier):

    def __init__(self, name, farbe, alter):
        Tier.__init__(self, name, farbe, alter)



    def reden(self, anzahl):
        print("Die Katze "+self.name+" miaut etwa "+anzahl+" Mal am Tag. "+self.name+" macht dabei MIAU")

    def fressen(self, mahlzeit, anzahl):
        print("Die Katze "+self.name+" isst dabei etwa "+anzahl+" Mahlzeiten. Es ist normales "+mahlzeit)


    def kuescheln(self,mensch):
        print("Die Katze "+self.name+" kueschelt dabei mit "+mensch+" 20 Mal pro Tag.")

    def _str_(self):
        print("")
        print("Kommen wir zur Katze " + self.name)
        self.schlafen("12")
        self.reden("100")
        self.fressen("Katzenfutter", "3")
        self.kuescheln("Keijo")

class Hund(Tier):
    def __init__(self, name, farbe, alter):
        Tier.__init__(self, name, farbe, alter)

    def reden(self, anzahl):
        print("Der Hund "+self.name+" bellt etwa "+anzahl+" Mal am Tag. "+self.name+" macht dabei WUFF WUFF")

    def fressen(self, mahlzeit, anzahl):
        print("Der Hund "+self.name+" isst dabei etwa "+anzahl+" Mahlzeiten. Es ist normales "+mahlzeit)

    def spielen(self, anzahl):
        print("Der Hund "+self.name+" möchte dabei etwa "+anzahl+" mal am Tag mit mir spielen.")

    def _str_(self):
        print("")
        print("Kommen wir zum Hund "+self.name)
        self.schlafen("14") #noch machen
        self.reden("100")
        self.fressen("Hundefutter", "3")
        self.spielen("20")


class main:
    x = Tier("Larry", "Sugarbrown", "4")
    x._str_()
    y = Katze("Mauzi", "Lightskinned", "15")
    y._str_()
    z = Hund("Doggi Dog", "Black", "4")
    z._str_()
class Auto():

    nopeus = 0

    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
    
    def kiihdyta(self, kiihdytys):
        Auto.nopeus = Auto.nopeus + kiihdytys
        if Auto.nopeus > self.huippunopeus:
            Auto.nopeus = self.huippunopeus
        elif Auto.nopeus < 0:
            Auto.nopeus = 0
        print(f"Uusi nopeus on: {self.nopeus}")

auto = Auto("ABC-123", 142)

print (f"Auton rekisteritunnus on: {auto.rekisteritunnus} ja huippunopeus oli: {auto.huippunopeus} km/h")

auto.kiihdyta(30)
auto.kiihdyta(70)
auto.kiihdyta(50)
auto.kiihdyta(-200)
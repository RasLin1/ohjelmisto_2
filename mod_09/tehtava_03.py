class Auto():

    nopeus = 0
    kuljettu_matka = 0

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
    
    def kulje(self, aika):
        Auto.kuljettu_matka = Auto.kuljettu_matka + (Auto.nopeus * aika)
        print(f"Tähän asti kuljettu matka on: {Auto.kuljettu_matka}")

auto = Auto("ABC-123", 142)

print (f"Auton rekisteritunnus on: {auto.rekisteritunnus} ja huippunopeus oli: {auto.huippunopeus} km/h")

auto.kiihdyta(30)
auto.kulje(0.5)
auto.kiihdyta(70)
auto.kulje(1.5)
auto.kiihdyta(50)
auto.kulje(1)
auto.kiihdyta(-200)
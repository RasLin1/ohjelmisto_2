import random

class Auto():
    def __init__(self, rekisteritunnus, huippunopeus, nopeus = 0, kuljettu_matka = 0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.kuljettu_matka = kuljettu_matka
    
    def kiihdyta(self, kiihdytys):
        self.nopeus = self.nopeus + kiihdytys
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0
    
    def kulje(self, aika):
        self.kuljettu_matka = self.kuljettu_matka + (self.nopeus * aika)

counter = 0
auto_maara = 10
allow_race  =  True
autot = []

while allow_race:
    if counter < auto_maara:
        rekisteri = f"ABC-{counter + 1}"
        huippunopeus = random.randint(100, 200)
        auto = Auto(rekisteri, huippunopeus)
        autot.append(auto)
        counter = counter + 1

    elif counter == auto_maara:
        for x in autot:
            if x.kuljettu_matka < 10000:
                kiihtymis_maara = random.randint (-10, 15)
                x.kiihdyta(kiihtymis_maara)
                x.kulje(1)
                print(f"{x.rekisteritunnus} on kulkenut {x.kuljettu_matka}")
            elif x.kuljettu_matka >= 10000:
                print(f"{x.rekisteritunnus} voitti!!")
                allow_race = False
        

    

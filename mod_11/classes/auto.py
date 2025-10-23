class Auto():
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0
        print("Auto created")
    
    def kiihdyta(self, kiihdytys):
        self.nopeus = self.nopeus + kiihdytys
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0
        
    
    def kulje(self, aika):
        self.kuljettu_matka = self.kuljettu_matka + (self.nopeus * aika)


class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, polttoainekapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.polttoainekapasiteetti = polttoainekapasiteetti
import random
from tabulate import tabulate

class Kilpailu():
    leading_distance = 0
    leading_reg = 0
    def __init__(self, name, distance, autot):
        self.name = name
        self.distance = distance
        self.autot = autot
        print(f"{self.name} alkaa")
    
    def tunti_kuluu(self):
        for auto in self.autot:
            auto.kiihdyta(random.randint (-10, 15))
            auto.kulje(1)
            if auto.kuljettu_matka > Kilpailu.leading_distance:
                Kilpailu.leading_distance = auto.kuljettu_matka
                Kilpailu.leading_reg = auto.rekisteritunnus
    
    def tulosta_tilanne(self):
        tulostettavat = []
        headers = ["Rekisteritunnus", "Kuljettu matka", "Nopeus"]
        for auto in self.autot:
            tulostettavat.append([auto.rekisteritunnus, f"{auto.kuljettu_matka} km", f"{auto.nopeus} km/h"])
        print(tabulate(tulostettavat, headers, tablefmt = "grid"))
        
    def kilpailu_ohi(self):
        return any(auto.kuljettu_matka > self.distance for auto in self.autot)
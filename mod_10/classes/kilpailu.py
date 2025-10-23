import random

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
        for auto in self.autot:
            print(f"{auto.rekisteritunnus} | {auto.kuljettu_matka} km | {auto.nopeus} km/h")
            print("")
        print("-------------------------------------------------")
        print("")
        
    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.kuljettu_matka > self.distance:
                return False
            else:
                return True
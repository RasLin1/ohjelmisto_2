import random
from auto import Auto

counter = 0
auto_amount = 10
allow_race  =  True
autot = []

while allow_race:
    if counter < auto_amount:
        rekisteri = f"ABC-{counter + 1}"
        huippunopeus = random.randint(100, 200)
        auto = Auto(rekisteri, huippunopeus)
        autot.append(auto)
        counter = counter + 1

    elif counter == auto_amount:
        for x in autot:
            if x.kuljettu_matka < 10000:
                kiihtymis_maara = random.randint (-10, 15)
                x.kiihdyta(kiihtymis_maara)
                x.kulje(1)
                print(f"{x.rekisteritunnus} on kulkenut {x.kuljettu_matka} km")
            elif x.kuljettu_matka >= 10000:
                print(f"{x.rekisteritunnus} voitti!!")
                allow_race = False
        

    

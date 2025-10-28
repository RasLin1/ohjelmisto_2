import random
from tabulate import tabulate
from auto import Auto

counter = 0
auto_amount = 10
allow_race  =  True
autot = []

leading_auto_rekisteri = 0
leading_auto_distance = 0

while allow_race:
    if counter < auto_amount:
        rekisteri = f"ABC-{counter + 1}"
        huippunopeus = random.randint(100, 200)
        auto = Auto(rekisteri, huippunopeus)
        autot.append(auto)
        counter = counter + 1

    elif counter == auto_amount:
        for auto in autot:
            kiihtymis_maara = random.randint (-10, 15)
            auto.kiihdyta(kiihtymis_maara)
            auto.kulje(1)
            if auto.kuljettu_matka > leading_auto_distance:
                leading_auto_rekisteri = auto.rekisteritunnus
                leading_auto_distance = auto.kuljettu_matka
                tulostettavat = []
                headers = ["Rekisteritunnus", "Kuljettu matka", "Nopeus"]
                for auto in autot:
                    tulostettavat.append([auto.rekisteritunnus, f"{auto.kuljettu_matka} km", f"{auto.nopeus} km/h"])
                print(tabulate(tulostettavat, headers, tablefmt = "grid"))
            if auto.kuljettu_matka >= 10000:
                allow_race = False
        

print(f"{leading_auto_rekisteri} voitti ja se kulki {leading_auto_distance} km")
        

    

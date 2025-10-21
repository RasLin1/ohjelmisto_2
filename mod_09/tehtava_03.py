from auto import Auto

auto = Auto("ABC-123", 142)

print (f"Auton rekisteritunnus on: {auto.rekisteritunnus} ja huippunopeus oli: {auto.huippunopeus} km/h")

auto.kiihdyta(30)
print(f"Uusi nopeus on: {auto.nopeus} km/h")
auto.kulje(0.5)
print(f"Tähän asti kuljettu matka on: {auto.kuljettu_matka} km")
auto.kiihdyta(70)
print(f"Uusi nopeus on: {auto.nopeus} km/h")
auto.kulje(1.5)
print(f"Tähän asti kuljettu matka on: {auto.kuljettu_matka} km")
auto.kiihdyta(50)
print(f"Uusi nopeus on: {auto.nopeus} km/h")
auto.kulje(1)
print(f"Tähän asti kuljettu matka on: {auto.kuljettu_matka} km")
auto.kiihdyta(-200)
print(f"Uusi nopeus on: {auto.nopeus} km/h")
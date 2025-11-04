from auto import Auto

auto = Auto("ABC-123", 142)

print (f"Auton rekisteritunnus on: {auto.rekisteritunnus} ja huippunopeus oli: {auto.huippunopeus} km/h")

auto.kiihdyta(30)
print(f"Uusi nopeus on: {auto.nopeus} km/h")
auto.kiihdyta(70)
print(f"Uusi nopeus on: {auto.nopeus} km/h")
auto.kiihdyta(50)
print(f"Uusi nopeus on: {auto.nopeus} km/h")
auto.kiihdyta(-200)
print(f"Uusi nopeus on: {auto.nopeus} km/h")
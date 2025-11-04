from mod_11.classes.auto import Sahkoauto, Polttomoottoriauto
import random

autot = []
autot.append(Sahkoauto("ABC-15", 180, 52.5))
autot.append(Polttomoottoriauto("ACD-123", 165, 32.3))

for a in autot:
    a.kiihdyta(random.randint(100, a.huippunopeus))

for x in range(3):
    for a in autot:
        a.kulje(1)

for a in autot:
    print(f"{a.rekisteritunnus} lopullinen mittarilukema: {a.kuljettu_matka}")
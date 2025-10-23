from mod_10.classes.auto import Auto
from mod_10.classes.kilpailu import Kilpailu
import random

counter = 0
auto_amount = 10
allow_race = True
autot = []

while counter < auto_amount:
    auto = Auto(f"ABC-{counter + 1}", random.randint(100, 200))
    autot.append(auto)
    counter = counter + 1

k = Kilpailu("Suuri romuralli", 8000, autot)

while allow_race:
    for x in range(10):
        k.tunti_kuluu()
        race_won = k.kilpailu_ohi()
    k.tulosta_tilanne()

if allow_race == False:
    k.tulosta_tilanne()
    print(f"{Kilpailu.leading_reg} voitti | kulki {Kilpailu.leading_distance} km")


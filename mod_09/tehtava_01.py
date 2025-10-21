class Auto():
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus

auto = Auto("ABC-123", 142)


print (f"Auton rekisteritunnus on: {auto.rekisteritunnus} ja huippunopeus oli: {auto.huippunopeus} km/h")
class Hissi():
    def __init__(self, lowest_floor, highest_floor, current_floor = 0):
        self.lowest_floor = lowest_floor
        self.highest_floor = highest_floor
        self.current_floor = current_floor

    def hissi_alas(self):
        self.current_floor = self.current_floor - 1
        print(f"Nykyinen kerros on {self.current_floor}")
    
    def hissi_ylos(self):
        self.current_floor = self.current_floor + 1
        print(f"Nykyinen kerros on {self.current_floor}")

h = Hissi(-1, 5)

while h.current_floor < 5:
    if h.current_floor <= h.highest_floor:
        h.hissi_ylos()
    else:
        print("Et voi mennä korkeamalle!")

if h.current_floor == 5:
    while h.current_floor > 0:
        h.hissi_alas()
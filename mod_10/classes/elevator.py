class Elevator():
    def __init__(self, number, lowest_floor, highest_floor, current_floor = 0):
        self.elevator_num = number
        self.lowest_floor = lowest_floor
        self.highest_floor = highest_floor
        self.current_floor = current_floor

    def elevator_down(self):
        self.current_floor = self.current_floor - 1
        print(f"Nykyinen kerros hissille {self.elevator_num} on {self.current_floor}")
    
    def elevator_up(self):
        self.current_floor = self.current_floor + 1
        print(f"Nykyinen kerros hissille {self.elevator_num} on {self.current_floor}")

class Elevator():
    def __init__(self, number, current_floor = 0):
        self_elevator_num = number
        self.current_floor = current_floor

    def elevator_down(self):
        self.current_floor = self.current_floor - 1
        print(f"Nykyinen kerros on {self.current_floor}")
    
    def elevator_up(self):
        self.current_floor = self.current_floor + 1
        print(f"Nykyinen kerros on {self.current_floor}")

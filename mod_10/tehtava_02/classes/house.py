from elevator import Elevator

class House():
    existing_elevators = 0
    def __init__(self, lowest_floor, highest_floor, elevator_amount):
        temp_elevators_holder = []
        while House.existing_elevators < elevator_amount:
            elevator = Elevator(House.existing_elevators + 1)
            temp_elevators_holder.append(elevator)
        self.lowest_floor = lowest_floor
        self.highest_floor = highest_floor
        self.elevators = temp_elevators_holder
from mod_10.classes.elevator import Elevator

class Building():
    existing_elevators = 0
    def __init__(self, lowest_floor, highest_floor, elevator_amount):
        temp_elevators_holder = []
        while Building.existing_elevators < elevator_amount:
            elevator = Elevator(Building.existing_elevators + 1, lowest_floor, highest_floor)
            temp_elevators_holder.append(elevator)
            Building.existing_elevators = Building.existing_elevators + 1
        self.lowest_floor = lowest_floor
        self.highest_floor = highest_floor
        self.elevators = temp_elevators_holder

    def move_elevator(self, elevator_number, new_floor):
        allow_movement = True
        while self.elevators[elevator_number - 1].current_floor != new_floor and allow_movement:
            if self.elevators[elevator_number - 1].current_floor > new_floor and self.elevators[elevator_number - 1].current_floor >= self.lowest_floor + 1:
                self.elevators[elevator_number - 1].elevator_down()
            elif self.elevators[elevator_number - 1].current_floor < new_floor and self.elevators[elevator_number - 1].current_floor <= self.highest_floor - 1:
                self.elevators[elevator_number - 1].elevator_up()
            else:
                print("ERROR: couldn't move the elevator")
                allow_movement = False

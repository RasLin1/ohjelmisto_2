<<<<<<< HEAD
from .elevator import Elevator
=======
from mod_10.classes.elevator import Elevator
>>>>>>> 055629f993c96d6bbdd0fe92507fb6cee6e3a844

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
<<<<<<< HEAD
    
    def move_elevator(self, elevator_number, new_floor):
        allow_movement = True
        while self.elevators[elevator_number - 1].current_floor != new_floor and allow_movement:
            if self.elevators[elevator_number - 1].current_floor >  new_floor and self.elevators[elevator_number - 1].current_floor >= self.elevators[elevator_number - 1].lowest_floor:
                self.elevators[elevator_number - 1].elevator_down()
            elif self.elevators[elevator_number - 1].current_floor <  new_floor and self.elevators[elevator_number - 1].current_floor <= self.elevators[elevator_number - 1].highest_floor:
                self.elevators[elevator_number - 1].elevator_up()
            else:
                allow_movement = False
                print("Annettu kerros ei sovi yhteen talon kanssa")
=======

    def move_building_elevator(self, elevator_number, new_floor):
        if self.elevators[elevator_number - 1].current_floor > new_floor:
            self.elevators[elevator_number - 1].elevator_down(new_floor)
        elif self.elevators[elevator_number - 1].current_floor < new_floor:
            self.elevators[elevator_number - 1].elevator_up(new_floor)
        else:
            print("ERROR: couldn't move the elevator")
    
    def fire_alarm(self):
        print("Palohälyytys!!!")
        print("Kaikki hissit pohjakerokkseen!!!")
        for x in range(Building.existing_elevators):
            self.elevators[x].elevator_down(self.lowest_floor)
>>>>>>> 055629f993c96d6bbdd0fe92507fb6cee6e3a844

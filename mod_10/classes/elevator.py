class Elevator():
    def __init__(self, number, lowest_floor, highest_floor, current_floor = 0):
        self.number = number
        self.lowest_floor = lowest_floor
        self.highest_floor = highest_floor
        self.current_floor = current_floor

    def move_elevator(self, new_floor):
        if new_floor > self.highest_floor or new_floor < self.lowest_floor:
             print("Anettu kerros on lian korkea tai matala")
        else:
            while self.current_floor != new_floor and self.current_floor >= self.lowest_floor:
                if self.current_floor > new_floor:
                    self.current_floor = self.current_floor - 1
                    print(f"Hissi numero {self.number} on nyt {self.current_floor} kerroksessa")
                elif self.current_floor < new_floor:
                    self.current_floor = self.current_floor + 1
                    print(f"Hissi numero {self.number} on nyt {self.current_floor} kerroksessa")

    def elevator_down(self, new_floor):
        while self.current_floor != new_floor and self.current_floor >= self.lowest_floor:
            self.current_floor = self.current_floor - 1
            print(f"Hissi numero {self.number} on nyt {self.current_floor} kerroksessa")
    
    def elevator_up(self, new_floor):
        while self.current_floor != new_floor:
            
                self.current_floor = self.current_floor + 1
                print(f"Hissi numero {self.number} on nyt {self.current_floor} kerroksessa")

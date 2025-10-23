from mod_10.classes.elevator import Elevator

h = Elevator(1, -1, 5)

<<<<<<< HEAD
while h.current_floor < 5:
    if h.current_floor <= h.highest_floor:
        h.elevator_up()
    else:
        print("Et voi mennä korkeamalle!")

if h.current_floor == 5:
    while h.current_floor > 0:
        h.elevator_down()
=======
h.move_elevator(5)
h.move_elevator(-1)
h.move_elevator(3)
>>>>>>> 055629f993c96d6bbdd0fe92507fb6cee6e3a844

from mod_10.classes.elevator import Elevator

h = Elevator(1, -1, 5)

while h.current_floor < 5:
    if h.current_floor <= h.highest_floor:
        h.elevator_up()
    else:
        print("Et voi mennä korkeamalle!")

if h.current_floor == 5:
    while h.current_floor > 0:
        h.elevator_down()
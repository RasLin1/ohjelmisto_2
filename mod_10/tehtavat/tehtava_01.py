from mod_10.classes.elevator import Elevator

h = Elevator(1, -1, 5)

while h.current_floor < 5:
    if h.current_floor <= h.highest_floor:
        h.move_elevator(h.highest_floor)
    else:
        print("Et voi mennä korkeamalle!")

if h.current_floor == 5:
    if h.current_floor <= h.highest_floor:
        h.move_elevator(0)
    else:
        print("Et voi mennä korkeamalle!")


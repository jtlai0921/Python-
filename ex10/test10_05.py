import math
force = True
move = 0
while(force):
    if move == 0:
        value = math.pi / move
        move += 10
    else:
        value = 0
        move = 0
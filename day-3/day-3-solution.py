## part 1
import numpy as np
# for testing only
# data_set = ['#1 @ 1,3: 4x4','#2 @ 3,1: 4x4','#3 @ 5,5: 2x2']

data_set = open("input-day-3.txt", "r").read().split("\n")[:-1]
rug = np.zeros((1000, 1000))

def fill_area(x, y, elf):
    if rug[x][y] == 0:
        rug[x][y] = elf
    else:
        rug[x][y] = -1

for row in data_set:
    values = row.split(" ")
    elf = int(values[0].split("#")[1])

    positions = values[2].split(",")

    from_left = int(positions[0])
    from_top = int(positions[1].split(":")[0])

    movement = values[3].split('x')
    move_right = int(movement[0])
    move_down = int(movement[1])

    for x in range(from_left, from_left + move_right):
        for y in range(from_top, from_top + move_down):
            fill_area(x, y, elf)

print(list(rug.flatten()).count(-1))

## part 2 - must be done after the full loop has iterated
for row in data_set:
    values = row.split(" ")
    elf = int(values[0].split("#")[1])
    movement = values[3].split('x')
    move_right = int(movement[0])
    move_down = int(movement[1])

    if list(rug.flatten()).count(elf) == move_right * move_down:
        print(elf)
        break;

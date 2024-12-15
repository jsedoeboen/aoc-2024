# file = open("small_input.txt", 'r')
# file = open("example_input.txt", 'r')
file =  open("input.txt", 'r')
map, moves = file.read().split("\n\n")
map = map.split("\n")

velocities = {
    '^': (0, -1),
    'v': (0, 1),
    '<': (-1, 0),
    '>': (1, 0)
}

height = len(map)
width = len(map[0])

grid = {}
robot = None

x = 0
while x < width * 2:
    for y in range(height):
        if map[y][x//2] == 'O':
            grid[x, y] = '['
            grid[x + 1, y] = ']'
        else:
            grid[x, y] = map[y][x//2]
            grid[x + 1, y] = map[y][x//2]
            if map[y][x//2] == '@':
                robot = (x, y)
                grid[x + 1, y] = '.'
    x += 2

def moveIntoNextPosition(item, velocity, cascade = True, check = False):
    x, y = item
    object = grid[x, y]
    v_x, v_y = velocity

    destination = (x + v_x, y + v_y)
    destination_object = grid[destination]

    # print("Evaluating (", check, ")", object, item, "to", destination_object, destination)

    if destination_object == '#':
        # print("Hit wall")
        return None
    elif (destination_object == '[' or destination_object == ']') and moveIntoNextPosition(destination, velocity, True, True) is None:
        return None

    d_x, d_y = destination

    blocked = False
    other_part = None
    if cascade and object == '[' and v_y != 0:
        other_part = (x + 1, y)
        # print("Checking for other part at", cascade, other_part)
        blocked = moveIntoNextPosition(other_part, velocity, False, True) is None
    elif cascade and object == ']' and v_y != 0:
        other_part = (x - 1, y)
        # print("Checking for other part at", cascade, other_part)
        blocked = moveIntoNextPosition(other_part, velocity, False, True) is None

    if not blocked and not check:
        if destination_object != '.':
            moveIntoNextPosition(destination, velocity)
        if other_part is not None: moveIntoNextPosition(other_part, velocity, False)

        print("Move", object, item, "to", destination_object, destination)

        grid[d_x, d_y] = grid[x, y]
        grid[x, y] = '.'
    elif blocked:
        return None

    return destination


# for y in range(height):
#     for x in range(width*2):
#         print(grid[x, y], end="")
#     print()

for i, move in enumerate(moves):
    if move not in velocities:
        continue

    print(i, move)

    new_pos = moveIntoNextPosition(robot, velocities[move])
    if new_pos is not None:
        robot = new_pos

    # for y in range(height):
    #     for x in range(width*2):
    #         print(grid[x, y], end="")
    #     print()

gps = 0
for (x,y) in grid:
    if grid[(x,y)] == '[':
        gps += 100 * y + x
print(gps)
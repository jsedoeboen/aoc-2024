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
for x in range(width):
    for y in range(height):
        grid[x, y] = map[y][x]
        if map[y][x] == '@':
            robot = (x, y)

def moveIntoNextPosition(item, velocity):
    x, y = item
    v_x, v_y = velocity

    destination = (x + v_x, y + v_y)
    destination_object = grid[destination]

    if destination_object == '#':
        return None
    elif destination_object == 'O' and moveIntoNextPosition(destination, velocity) is None:
        return None

    d_x, d_y = destination

    grid[d_x, d_y] = grid[x, y]
    grid[x, y] = '.'

    return destination


for move in moves:
    if move not in velocities:
        continue

    new_pos = moveIntoNextPosition(robot, velocities[move])
    if new_pos is not None:
        robot = new_pos

    # print(move)
    # for y in range(height):
    #     for x in range(width):
    #         print(grid[x, y], end="")
    #     print()

gps = 0
for (x,y) in grid:
    if grid[(x,y)] == 'O':
        gps += 100 * y + x
print(gps)
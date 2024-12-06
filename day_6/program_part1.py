# file = open("example_input.txt", 'r')
file =  open("input.txt", 'r')
lines = file.readlines()

height = len(lines)
width = len(lines[0]) - 1

grid = {}
for x in range(width):
    for y in range(height):
        grid[x, y] = lines[y][x]


def step(location, direction):
    # print(f"Location: {location}, Direction: {direction}")
    dx, dy = direction
    new_location = tuple(map(sum, zip(location, direction)))
    if grid.get(new_location) == "#":
        return step(location, (-dy, dx))
    return new_location, direction


def solve():
    visited = set()
    location, = (k for k, v in grid.items() if v == "^")
    direction = (0, -1)
    while location in grid:
        visited.add(location)
        location, direction = step(location, direction)
    return visited

visited_list = solve()
print("Path length: ", len(visited_list))

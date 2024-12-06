# file = open("example_input.txt", 'r')
file =  open("input.txt", 'r')
lines = file.readlines()

height = len(lines)
width = len(lines[0]) - 1

grid = {}
for x in range(width):
    for y in range(height):
        grid[x, y] = lines[y][x]


def step(location, direction, obstacle):
    # print(f"Location: {location}, Direction: {direction}")
    dx, dy = direction
    new_location = tuple(map(sum, zip(location, direction)))
    if grid.get(new_location) == "#" or new_location == obstacle:
        return step(location, (-dy, dx), obstacle)
    return new_location, direction


def solve(obstacle=None):
    visited = set()
    visited_incl_direction = set()
    location, = (k for k, v in grid.items() if v == "^")
    direction = (0, -1)
    while location in grid:
        # Break if we reach a loop
        if (location,direction) in visited_incl_direction:
            return None

        visited_incl_direction.add((location,direction))
        visited.add(location)
        location, direction = step(location, direction, obstacle)
    return visited

visited_list = solve()
print("Path length: ", len(visited_list))

loop_positions = []
for obstacle in visited_list:
    if(solve(obstacle) == None):
        loop_positions.append(obstacle)

print("Loop positions: ", loop_positions)
print("Loop count: ", len(loop_positions))
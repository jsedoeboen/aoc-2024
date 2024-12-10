MAX_INCREASE = 1

# file = open("example_input.txt", 'r')
file =  open("input.txt", 'r')
lines = file.readlines()

height = len(lines)
width = len(lines[0]) - 1

trail_heads = []
grid = {}
for x in range(width):
    for y in range(height):
        grid[x, y] = int(lines[y][x])
        if grid[x, y] == 0:
            trail_heads.append((x, y))

trails_map = {}
def find_next_node(node, trail):
    x, y = node

    if grid[x, y] == 9:
        print(f"Trail head {node} can reach 9 at {(x, y)} with max distance {MAX_INCREASE}")
        if trail[0] in trails_map:
            trails_map[trail[0]].append(trail)
        else:
            trails_map[trail[0]] = [trail]
        return

    for dx, dy in ((0, 1),(0, -1),(-1, 0),(1, 0)):
        next_pos_x = x + dx
        next_pos_y = y + dy

        if (next_pos_x, next_pos_y) not in grid:
            continue

        if grid[next_pos_x, next_pos_y] - grid[x, y] == 1:
            find_next_node((next_pos_x, next_pos_y), trail + [(next_pos_x, next_pos_y)])

for trail_head in trail_heads:
    find_next_node(trail_head, [trail_head])

sum = 0
for trail_head in trail_heads:
    summits = set()
    if trail_head in trails_map:
        for trail in trails_map[trail_head]:
            if trail[-1] not in summits:
                sum += 1
                summits.add(trail[-1])

print(f"Total number of trails: {sum}")
# file = open("example_input.txt", 'r')
file =  open("input.txt", 'r')
lines = file.readlines()

height = len(lines)
width = len(lines[0]) - 1

grid = {}
for x in range(width):
    for y in range(height):
        grid[x, y] = lines[y][x]

def calc_sides(border_plants):
    sides = []
    while border_plants:
        plant, out_direction = border_plants.pop()
        side = [(plant,out_direction)]
        (di, dj) = out_direction

        right = (dj, -di)
        right_plant = (plant[0] + right[0], plant[1] + right[1])
        while (right_plant,out_direction) in border_plants:
            border_plants.remove((right_plant, out_direction))
            side.append((right_plant,out_direction))
            right_plant = (right_plant[0] + right[0], right_plant[1] + right[1])

        left = (-dj, di)
        left_plant =  (plant[0] + left[0], plant[1] + left[1])
        while (left_plant,out_direction) in border_plants:
            border_plants.remove((left_plant, out_direction))
            side.append((left_plant,out_direction))
            left_plant =  (left_plant[0] + left[0], left_plant[1] + left[1])

        sides.append(side)
    return len(sides)

total_price = 0
visited_plants = set()
for plant,plant_type in grid.items():
    if plant in visited_plants:
        continue

    plant_region = {plant}

    border = set()
    queue = {plant}
    while queue:
        current_plant = queue.pop()
        for d in (0,1),(1,0),(0,-1),(-1,0):
            next_plant = (current_plant[0] + d[0], current_plant[1] + d[1])
            if grid.get(next_plant) == plant_type:
                if next_plant not in visited_plants:
                    queue.add(next_plant)
                    plant_region.add(next_plant)
                    visited_plants.add(next_plant)
            else:
                border.add((current_plant, d))
    total_price += calc_sides(border) * len(plant_region)

print(total_price)
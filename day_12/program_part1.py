# file = open("example_input.txt", 'r')
file =  open("input.txt", 'r')
lines = file.readlines()

height = len(lines)
width = len(lines[0]) - 1

grid = {}
for x in range(width):
    for y in range(height):
        grid[x, y] = lines[y][x]

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
                border.add(current_plant)
    total_price += len(border) * len(plant_region)

print(total_price)
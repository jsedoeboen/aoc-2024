# file = open("example_input.txt", 'r')
file =  open("input.txt", 'r')
lines = file.readlines()

antennas = {}
height = len(lines)
width = len(lines[0])-1

for x in range(width):
    for y in range(height):
        ch = lines[y][x]
        if ch == '.': continue
        if ch not in antennas:
            antennas[ch] = [(x,y)]
        else:
            antennas[ch].append((x,y))

anti_antennas = set()
for(antenna, coords) in antennas.items():
    for i in range(len(coords)):
        for j in range(len(coords)):
            if i == j: continue

            antenna_coords = coords[i]
            antenna_partner_coords = coords[j]

            # Difference between the two antennas
            dx = antenna_partner_coords[0] - antenna_coords[0]
            dy = antenna_partner_coords[1] - antenna_coords[1]

            # Calculate the two anti-antennas
            first_anti = antenna_partner_coords
            second_anti = antenna_coords
            # print(f"antenna: {antenna} {antenna_coords} {antenna_partner_coords}")

            # check if in grid
            while 0 <= first_anti[0] < width and 0 <= first_anti[1] < height:
                anti_antennas.add(first_anti)
                first_anti = (first_anti[0] + dx, first_anti[1] + dy)

            while 0 <= second_anti[0] < width and 0 <= second_anti[1] < height:
                anti_antennas.add(second_anti)
                second_anti = (second_anti[0] - dx, second_anti[1] - dy)


# print(f"w: {width} h: {height}")
print(anti_antennas)
print(len(anti_antennas))

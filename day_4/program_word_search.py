from re import search

WORD = "XMAS"

# file =  open("example_input.txt", 'r')
file =  open("input.txt", 'r')
lines = file.readlines()

height = len(lines)
width = len(lines[0])-1

grid = {}
for x in range(width):
    for y in range(height):
        grid[x, y] = lines[y][x]

count = 0
for x, y in grid:
    if grid[x, y] == WORD[0]: # If the first letter of the word is found
        for dx, dy in ((0, 1),(0, -1),(-1, 0),(1, 0), (1, 1),(-1,-1),(1, -1),(-1, 1)):
            word = ""
            for i in range(len(WORD)):
                next_pos_x = x + i * dx
                next_pos_y = y + i * dy
                if (next_pos_x, next_pos_y) not in grid:
                    break
                word += grid[next_pos_x, next_pos_y]
            # print(f"{word} at ({x}, {y} with direction ({dx}, {dy})")
            if word == WORD:
                print(f"Found {word} at ({x}, {y} with direction ({dx}, {dy})")
                count += 1

print(f"Word count: {count}")
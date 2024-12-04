from audioop import reverse

WORD = "MAS"

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
    if grid[x, y] == "A": # middle letter of the word
        firstDiagonal = grid.get((x-1,y-1),"") + "A" + grid.get((x+1,y+1),"")
        secondDiagonal = grid.get((x-1,y+1),"") + "A" + grid.get((x+1,y-1),"")
        if (firstDiagonal == WORD or firstDiagonal == WORD[::-1]) and (secondDiagonal == WORD or secondDiagonal == WORD[::-1]):
            print(f"Found at ({x}, {y})")
            count += 1

print(f"Word count: {count}")
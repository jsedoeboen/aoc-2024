# file = open("example_input.txt", 'r')
file =  open("input.txt", 'r')
line = file.readline()

stones = list(map(int, line.split(' ')))

memory = {}

def blink(stone, iterations):
    if iterations == 0:
        return 1
    elif (stone, iterations) in memory:
        return memory[(stone, iterations)]
    elif stone == 0:
        val = blink(1, iterations - 1)
    elif len(str_stone := str(stone)) % 2 == 0:
        mid = len(str_stone) // 2
        val = blink(int(str_stone[:mid]), iterations - 1) + blink(int(str_stone[mid:]), iterations - 1)
    else:
        val = blink(stone * 2024, iterations - 1)
    memory[(stone, iterations)] = val
    return val

result = sum(blink(stone, 75) for stone in stones)

print(result)
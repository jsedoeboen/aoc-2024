# file = open("example_input.txt", 'r')
file =  open("input.txt", 'r')
line = file.readline()

stones = list(map(int, line.split(' ')))

def blink_stone(stone):
    if stone == 0:
        return [1]
    stone_str = str(stone)
    length = len(stone_str)
    if length%2==0:
        return [int(stone_str[:length//2]),int(stone_str[length//2:])]
    else:
        return [2024*stone]

def blink(stones):
    i = 0
    while i < len(stones):
        new_stone = blink_stone(stones[i])
        stones = stones[:i] + new_stone + stones[i+1:]
        i += len(new_stone)
    return stones

for i in range(25):
    print("blink", i)
    stones = blink(stones)


# print(stones)
print(len(stones))

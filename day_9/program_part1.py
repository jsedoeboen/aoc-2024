# file = open("example_input.txt", 'r')
file =  open("input.txt", 'r')
line = file.readline()

blocks = []
id = 0
for i in range(len(line)):
    block_size = int(line[i])
    if i % 2:
        blocks += block_size * ['.']
    else:
        blocks += block_size * [id]
        id += 1

# print(blocks)

left_pointer = 0
right_pointer = len(blocks) - 1
while left_pointer <= right_pointer:
    if blocks[left_pointer] != '.':
        left_pointer += 1
    elif blocks[right_pointer] != '.':
        blocks[left_pointer] = blocks[right_pointer]
        blocks[right_pointer] = '.'

        left_pointer += 1
        right_pointer -= 1
    else:
        right_pointer -= 1

checksum = 0
for i in range(len(blocks)):
    checksum += i * blocks[i] if blocks[i] != '.' else 0

# print(blocks)
print(checksum)
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

print(blocks)

right_pointer = len(blocks) - 1
while 0 <= right_pointer:
    if blocks[right_pointer] == '.':
        right_pointer -= 1
        continue

    id = blocks[right_pointer]
    size = 0
    end_index = right_pointer
    while blocks[right_pointer] == id:
        size += 1
        right_pointer -= 1
    start_index = right_pointer + 1

    # print(f"{id} size: {size}, start_index: {start_index}, end_index: {end_index}")

    left_pointer = 0
    free = 0
    while left_pointer <= right_pointer:
        free = free + 1 if blocks[left_pointer] == '.' else 0
        if free >= size:
            blocks[left_pointer - free + 1:left_pointer - free + size + 1] = blocks[start_index:end_index+1]
            blocks[start_index:end_index+1] = size * ['.']
            break
        left_pointer += 1

checksum = 0
for i in range(len(blocks)):
    checksum += i * blocks[i] if blocks[i] != '.' else 0

# print(blocks)
print(checksum)
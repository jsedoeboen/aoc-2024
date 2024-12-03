import re

REGEX = r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))"

# file =  open("example_input.txt", 'r')
file =  open("input.txt", 'r')
lines = file.readlines()

sum = 0
enabled = True

for line in lines:
    for a, b, do, dont in re.findall(REGEX, line):
        if do or dont:
            enabled = bool(do)
        else:
            sum += (int(a) * int(b) * enabled)

print(f"Sum: {sum}")
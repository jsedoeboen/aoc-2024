import re

REGEX = r"mul\((\d+),(\d+)\)"

# file =  open("example_input.txt", 'r')
file =  open("input.txt", 'r')
lines = file.readlines()

sum = 0
for line in lines:
    for a, b in re.findall(REGEX, line):
        print(f"Result: {a}, {b}")
        sum += int(a) * int(b)

print(f"Sum: {sum}")
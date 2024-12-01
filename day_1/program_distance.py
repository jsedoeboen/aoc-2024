input_a = []
input_b = []

file =  open("input.txt", 'r')
lines = file.readlines()

for line in lines:
    splitLine = line.split(" ")
    input_a.append(int(splitLine[0].strip()))
    input_b.append(int(splitLine[-1].strip()))

input_a.sort()
input_b.sort()

print(f"input a: {input_a}")
print(f"input b: {input_b}")

distance = 0

for lineA, lineB in zip(input_a, input_b):
    distance += abs(lineA - lineB)

print(f"Distance: {distance}")



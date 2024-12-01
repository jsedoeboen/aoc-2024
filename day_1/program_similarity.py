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

similarity = 0

for lineA in input_a:
    similarity += lineA * input_b.count(lineA)

print(f"Similarity: {similarity}")



# file = open("example_input.txt", 'r')
file =  open("input.txt", 'r')
lines = file.readlines()

# first line is the number of towels the rest is the designs
towelList, designs = lines[0], lines[1:]
towels = towelList.split(', ')


cache = {}

def matchDesign(design, towels):
    if design == "":
        return 1

    if design in cache:
        return cache[design]

    sum = 0
    for i in range(len(towels)):
        towel = towels[i].strip()
        if design.startswith(towel):
            sum += matchDesign(design[len(towel):], towels)

    cache[design] = sum
    return sum


total = 0

for design in designs:
    design = design.strip()

    if design == "":
        continue

    matches = matchDesign(design, towels)
    # print(f"Design {design} could be matched with {matches} combinations)")
    total += matches

print(total)
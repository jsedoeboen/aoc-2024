# file = open("example_input.txt", 'r')
file =  open("input.txt", 'r')
lines = file.readlines()

# first line is the number of towels the rest is the designs
towelList, designs = lines[0], lines[1:]
towels = towelList.split(', ')


cache = {}

def matchDesign(design, towels):
    if design == "":
        return True

    if design in cache:
        return cache[design]

    for i in range(len(towels)):
        towel = towels[i]
        if design.startswith(towel):
            if matchDesign(design[len(towel):], towels):
                cache[design] = True
                return True

    cache[design] = False
    return False


total = 0

for design in designs:
    design = design.strip()

    if design == "":
        continue

    # what combination of towels matches the design
    couldMatch = matchDesign(design, towels)
    # if couldMatch:
    #     print(f"Design {design} could be matched with {couldMatch} combinations)")

    total += 1 if couldMatch else 0

print(total)
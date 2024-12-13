# file = open("example_input.txt", 'r')
file =  open("input.txt", 'r')
lines = file.readlines()

tokens = 0
for line in lines:
    if line.strip() == "":
        continue

    line_type, values = line.split(":")

    if line_type.startswith("Button"):
        _, label = line_type.split(" ")

        values = values.split(",")

        if label == 'A':
            a_x = int(values[0].split("+")[-1].strip())
            a_y = int(values[1].split("+")[-1].strip())
        else:
            b_x = int(values[0].split("+")[-1].strip())
            b_y = int(values[1].split("+")[-1].strip())

    elif line_type.startswith("Prize"):
        values = values.split(",")
        prize_x = 10000000000000 + int(values[0].split("=")[-1].strip())
        prize_y = 10000000000000 + int(values[1].split("=")[-1].strip())

        outputs = []
        b = (prize_x*a_y-prize_y*a_x)//(a_y*b_x-b_y*a_x)
        a = (prize_x*b_y-prize_y*b_x)//(b_y*a_x-b_x*a_y)
        if a_x*a+b_x*b==prize_x and a_y*a+b_y*b==prize_y:
            tokens += 3*a+b

print(tokens)

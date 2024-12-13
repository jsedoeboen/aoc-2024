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
        prize_x = int(values[0].split("=")[-1].strip())
        prize_y = int(values[1].split("=")[-1].strip())

        outputs = []
        for a in range(100):
            for b in range(100):
                if a_x*a+b_x*b==prize_x and a_y*a+b_y*b==prize_y:
                    outputs.append(3*a+b)
        if outputs:
            tokens += min(outputs)

print(tokens)

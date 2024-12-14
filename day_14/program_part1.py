# file = open("example_input.txt", 'r')
file =  open("input.txt", 'r')
lines = file.readlines()

iterations = 100
width = 101
height = 103
x_mid = width // 2
y_mid = height // 2
quadrant1, quadrant2, quadrant3, quadrant4 = 0, 0, 0, 0

for line in lines:
    values = line.split(' ')

    p = values[0].split('=')[-1]
    v = values[1].split('=')[-1]

    p_x = int(p.split(',')[0])
    p_y = int(p.split(',')[1])

    v_x = int(v.split(',')[0])
    v_y = int(v.split(',')[1])

    x_final = (p_x + v_x * iterations) % width
    y_final = (p_y + v_y * iterations) % height

    if x_final < x_mid and y_final < y_mid:
        quadrant1 += 1
    elif x_final < x_mid and y_final > y_mid:
        quadrant2 += 1
    elif x_final > x_mid and y_final < y_mid:
        quadrant3 += 1
    elif x_final > x_mid and y_final > y_mid:
        quadrant4 += 1

print(quadrant1 * quadrant2 * quadrant3 * quadrant4)
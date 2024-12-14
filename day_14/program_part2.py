# file = open("example_input.txt", 'r')
file =  open("input.txt", 'r')
lines = file.readlines()

iterations = 100
width = 101
height = 103
x_mid = width // 2
y_mid = height // 2

class Robot:
    def __init__(self, p_x, p_y, v_x, v_y):
        self.position = (p_x, p_y)
        self.velocity = (v_x, v_y)

robots = []
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

    robots.append(Robot(p_x, p_y, v_x, v_y))


def print_map(robots):
    map = [['.' for _ in range(width)] for _ in range(height)]
    for robot in robots:
        x, y = robot.position
        map[y][x] = '#'

    for row in map:
        print(''.join(row))

T = 0
while True:
    distinct_positions = set(map(lambda r: r.position, robots))

    # Geen overlap
    if len(distinct_positions) == len(robots):
        break

    for robot in robots:
        px, py = robot.position
        vx, vy = robot.velocity

        robot.position = ((px + vx) % width, (py + vy) % height)

    T += 1

print_map(robots)

print(T)

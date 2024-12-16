from heapq import *

# file = open("example_input.txt", 'r')
file =  open("input.txt", 'r')
lines = file.readlines()

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

height = len(lines)
width = len(lines[0]) -1

def dijkstra(grid, start, end):
    costs = {(start, 1): 0}
    pq = [(0, (start, 1))]
    while pq:
        cost, (node, direction) = heappop(pq)
        if cost != costs[(node, direction)]:
            continue
        if node == end:
            return cost
        node_x, node_y = node

        # move
        d_x, d_y = directions[direction]
        next_node_x, next_node_y = node_x + d_x, node_y + d_y

        if grid[next_node_x, next_node_y] != "#":
            if 0 <= next_node_x < height and 0 <= next_node_y < width:
                next_node = ((next_node_x, next_node_y), direction)
                if next_node not in costs or costs[next_node] > cost + 1:
                    costs[next_node] = cost + 1
                    heappush(pq, (cost + 1, next_node))

        # rotate
        rotate_left = (direction - 1) % 4
        next_node = ((node_x, node_y), rotate_left)
        if next_node not in costs or costs[next_node] > cost + 1000:
            costs[next_node] = cost + 1000
            heappush(pq, (cost + 1000, next_node))

        rotate_right = (direction + 1) % 4
        next_node = ((node_x, node_y), rotate_right)
        if next_node not in costs or costs[next_node] > cost + 1000:
            costs[next_node] = cost + 1000
            heappush(pq, (cost + 1000, next_node))

grid = {}
reindeer = None
target = None
for x in range(width):
    for y in range(height):
        grid[x, y] = lines[y][x]
        if lines[y][x] == 'S':
            reindeer = (x, y)
        if lines[y][x] == 'E':
            target = (x, y)

print(dijkstra(grid, reindeer, target))
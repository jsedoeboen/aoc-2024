from heapq import *

# file = open("example_input.txt", 'r')
file =  open("input.txt", 'r')
lines = file.readlines()

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

height = len(lines)
width = len(lines[0]) -1

def dijkstra(grid, start, end):
    costs = {(start, 1): (0, [None])}
    pq = [(0, (start, 1))]
    while pq:
        cost, (node, direction) = heappop(pq)
        if cost != costs[(node, direction)][0]:
            continue
        if node == end:
            return costs, (node, direction)
        node_x, node_y = node

        # move
        d_x, d_y = directions[direction]
        next_node_x, next_node_y = node_x + d_x, node_y + d_y

        if grid[next_node_x, next_node_y] != "#":
            if 0 <= next_node_x < height and 0 <= next_node_y < width:
                next_node = ((next_node_x, next_node_y), direction)
                if next_node in costs and costs[next_node][0] == cost + 1:
                    costs[next_node] = (cost + 1, costs[next_node][1] + [(node, direction)])
                    heappush(pq, (cost + 1, next_node))
                elif next_node not in costs or costs[next_node][0] > cost + 1:
                    costs[next_node] = (cost + 1, [(node, direction)])
                    heappush(pq, (cost + 1, next_node))

        # rotate
        rotate_left = (direction - 1) % 4
        next_node = ((node_x, node_y), rotate_left)
        if next_node in costs and costs[next_node][0] == cost + 1000:
            costs[next_node] = (cost + 1000, costs[next_node][1] + [(node, direction)])
            heappush(pq, (cost + 1000, next_node))
        elif next_node not in costs or costs[next_node][0] > cost + 1000:
            costs[next_node] = (cost + 1000, [(node, direction)])
            heappush(pq, (cost + 1000, next_node))

        rotate_right = (direction + 1) % 4
        next_node = ((node_x, node_y), rotate_right)
        if next_node in costs and costs[next_node][0] == cost + 1000:
            costs[next_node] = (cost + 1000, costs[next_node][1] + [(node, direction)])
            heappush(pq, (cost + 1000, next_node))
        elif next_node not in costs or costs[next_node][0] > cost + 1000:
            costs[next_node] = (cost + 1000, [(node, direction)])
            heappush(pq, (cost + 1000, next_node))

def backtrack_path(costs, path):
    prev_nodes = costs[path[-1]][1]
    total_nodes = set()
    for prev_node in prev_nodes:
        if prev_node is None:
            total_nodes.add(path[-1][0])
        else:
            path = path + tuple([prev_node])
            if prev_node[0] not in total_nodes:
                p = backtrack_path(costs, path)
                p.add(path[-1][0])
                total_nodes |= p

    return total_nodes

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

costs, end_state = dijkstra(grid, reindeer, target)
path = backtrack_path(costs, tuple([end_state]))

# for x, y in path:
#     grid[x, y] = "O"

# for y in range(height):
#     for x in range(width):
#         print(grid[x, y], end="")
#     print()

print(len(path))
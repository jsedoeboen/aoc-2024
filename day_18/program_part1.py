# file = open("example_input.txt", 'r')
file =  open("input.txt", 'r')
lines = file.readlines()
bytes = [(int(line.split(",")[0]), int(line.split(",")[1])) for line in lines]

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

max_width = 70
max_height = 70

start = (0, 0)
end = (max_width, max_height)

def bfs(i, end):
    # all bytes are blocked so we can't visit them
    visited = set(bytes[:i])

    queue = [(0, (0, 0))]

    while queue:
        dist, pos = queue.pop(0)

        if pos == end:
            return dist

        if pos in visited:
            continue

        print(pos)

        for direction in directions:
            next_pos = (pos[0] + direction[0], pos[1] + direction[1])

            if next_pos in visited:
                continue

            if 0<=next_pos[0]<=max_width and 0<=next_pos[1]<=max_height:
                visited.add(pos)
                queue.append((dist + 1, next_pos))

print(bfs(1024, end))
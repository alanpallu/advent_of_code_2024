
def part1():
    with open("files/day6.txt") as f:
        data = [line.strip() for line in f]
        data = [list(line) for line in data]

    r = len(data)
    c = len(data[0])
    guard_position = (0,0)
    res = 0
    obstacles = []
    guard_path = [(-1,0), (0, 1), (1, 0), (0, -1)]
    already_visited = []

    for i in range(r):
        for j in range(c):
            if data[i][j] == "^":
                guard_position = (i, j)
            elif data[i][j] == "#":
                obstacles.append((i, j))

    pos = 0
    while True:
        path = guard_path[pos]
        new_guard_position = (guard_position[0] + path[0], guard_position[1] + path[1])
        if new_guard_position[0] > r or new_guard_position[1] > c or new_guard_position[0] < 0 or new_guard_position[1] < 0:
            break
        if new_guard_position in obstacles:
            pos = pos + 1 if pos != 3 else 0
        else:
            guard_position = new_guard_position
            if guard_position not in already_visited:
                res += 1
                already_visited.append(guard_position)

    return res

def part2():
    with open("files/day6.txt") as f:
        data = [line.strip() for line in f]
        data = [list(line) for line in data]

    r = len(data)
    c = len(data[0])
    guard_position = (0,0)
    res = 0
    obstacles = []
    grid = []
    guard_path = [(-1,0), (0, 1), (1, 0), (0, -1)]
    already_visited = []

    for i in range(r):
        for j in range(c):
            if data[i][j] == "^":
                guard_position = (i, j)
            elif data[i][j] == "#":
                obstacles.append((i, j))
            else:
                grid.append((i, j))

    initial_guard_position = (guard_position[0], guard_position[1])
    pos = 0
    while True:
        path = guard_path[pos]
        new_guard_position = (guard_position[0] + path[0], guard_position[1] + path[1])
        if new_guard_position[0] > r or new_guard_position[1] > c or new_guard_position[0] < 0 or new_guard_position[
            1] < 0:
            break
        if new_guard_position in obstacles:
            pos = pos + 1 if pos != 3 else 0
        else:
            guard_position = new_guard_position
            if guard_position not in already_visited:
                already_visited.append(guard_position)

    def will_loop(coords):
        pos = 0
        visited_loop = []
        guard_position = initial_guard_position
        i = coords[0]
        j = coords[1]
        obstacles.append((i, j))
        while True:
            path = guard_path[pos]
            new_guard_position = (guard_position[0] + path[0], guard_position[1] + path[1])
            if new_guard_position[0] > r or new_guard_position[1] > c or new_guard_position[0] < 0 or \
                    new_guard_position[
                        1] < 0:
                obstacles.remove((i, j))
                return False
            if new_guard_position in obstacles:
                pos = pos + 1 if pos != 3 else 0
            else:
                guard_position = new_guard_position
                if (new_guard_position[0], new_guard_position[1], path) not in visited_loop:
                    visited_loop.append((new_guard_position[0], new_guard_position[1], path))
                else:
                    obstacles.remove((i, j))
                    return True

    for coord in grid:
        if will_loop(coord):
            res += 1

    return res


if __name__ == "__main__":
    res = part2()
    print(res)
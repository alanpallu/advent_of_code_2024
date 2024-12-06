
def part1():
    with open("files/day4.txt") as f:
        data = f.readlines()

    r = len(data)
    c = len(data[0]) - 1
    directions = [(1,0), (0,-1), (0,1), (-1,0), (1,-1), (-1,-1), (-1,1), (1,1)]

    word = "XMAS"
    res = 0

    for i in range(r):
        for j in range(c):
            if data[i][j] == 'X':
                for dx, dy in directions:
                    if 0 <= i + 3 * dx < r and 0 <= j + 3 * dy < c:
                        if data[i][j] + data[i + dx][j + dy] + data[i + dx * 2][j + dy * 2] + data[i + dx * 3][j + dy * 3] == word:
                            res += 1

    return res

def part2():
    with open("files/day4.txt") as f:
        data = f.readlines()

    r = len(data)
    c = len(data[0]) - 1
    word = 'MAS'
    res = 0

    for i in range(1, r - 1):
        for j in range(1, c - 1):
            if data[i][j] == 'A':
                if ((data[i - 1][j - 1] + data[i][j] + data[i + 1][j + 1] == word or data[i + 1][j + 1] + data[i][j] + data[i - 1][j - 1] == word)
                    and (data[i - 1][j + 1] + data[i][j] + data[i + 1][j - 1] == word or data[i + 1][j - 1] + data[i][j] +data[i - 1][j + 1] == word)):
                    res += 1

    return res

if __name__ == '__main__':
    res = part2()
    print(res)

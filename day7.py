import itertools

def part1():
    with open("files/day7.txt") as f:
        data = [line.strip() for line in f]
        data = [line.replace(':', '') for line in data]
        data = [line.split(' ') for line in data]

    res = 0
    for line in data:
        result = int(line.pop(0))
        line = [int(element) for element in line]
        n = len(line)
        combinations = itertools.product(['+', '*'], repeat=n-1)

        for comb in combinations:
            aux = line[0]
            for i in range(1, n):
                if comb[i-1] == '+':
                    aux +=  line[i]
                elif comb[i-1] == '*':
                    aux *= line[i]
            if aux == result:
                res += result
                break

    return res

def part2():
    with open("files/day7.txt") as f:
        data = [line.strip() for line in f]
        data = [line.replace(':', '') for line in data]
        data = [line.split(' ') for line in data]

    res = 0
    for line in data:
        result = int(line.pop(0))
        line = [int(element) for element in line]
        n = len(line)
        combinations = itertools.product(['+', '*', 'l'], repeat=n-1)

        for comb in combinations:
            aux = line[0]
            for i in range(1, n):
                if comb[i-1] == '+':
                    aux +=  line[i]
                elif comb[i-1] == '*':
                    aux *= line[i]
                elif comb[i-1] == 'l':
                    aux = int(str(aux) + str(line[i]))
            if aux == result:
                res += result
                break

    return res

if __name__ == "__main__":
    part1 = part1()
    part2 = part2()
    print(part2)
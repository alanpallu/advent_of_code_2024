
def main():
    with open("files/day2.txt") as f:
        data = f.readlines()

    safe = 0
    for line in data:
        parsed_line = line.split()
        parsed_line = [int(a) for a in parsed_line]
        new_line = parsed_line
        for i in range(len(parsed_line) + 1):
            if is_safe(new_line):
                safe += 1
                break
            else:
                new_line = parsed_line[:i] + parsed_line[i+1:]

    return safe

def is_safe(line):
    aux = 0
    length = len(line)
    for i in range(length - 1):
        cresc = all(line[i] < line[i + 1] for i in range(len(line) - 1))
        decresc = all(line[i] > line[i + 1] for i in range(len(line) - 1))
        curr_el = line[i]
        next_el = line[i + 1]
        diff = abs(next_el - curr_el)
        if 3 >= diff >= 1 and (cresc or decresc):
            aux += 1

    if length - 1 == aux:
        return True

    return False

if __name__ == '__main__':
    res = main()
    print(res)
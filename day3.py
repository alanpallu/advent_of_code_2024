
import re
def part1():
    with open("files/day3.txt") as f:
        data = f.read()

    result = 0
    text = re.findall("mul\((-?\d+),(-?\d+)\)", data)
    for item in text:
        result += int(item[0])*int(item[1])

    return result

def part2():
    with open("files/day3.txt") as f:
        data = f.read()

    result = 0

    mul_pattern = re.compile(r'mul\((-?\d+),(-?\d+)\)')
    dont_pattern = re.compile(r"don't\(\)")
    do_pattern = re.compile(r"do\(\)")

    mul_matches = [(match.start(), match.end(), match.group(1), match.group(2)) for match in mul_pattern.finditer(data)]
    dont_matches = [match.start() for match in dont_pattern.finditer(data)]
    do_matches = [match.start() for match in do_pattern.finditer(data)]

    for mul_start, mul_end, num1_str, num2_str in mul_matches:
        include_mul = True

        last_dont = None
        for dont_pos in dont_matches:
            if dont_pos < mul_start:
                last_dont = dont_pos
            else:
                break

        if last_dont is not None:
            do_between = any(last_dont < do_pos < mul_start for do_pos in do_matches)
            if not do_between:
                include_mul = False

        if include_mul:
            result += int(num1_str) * int(num2_str)

    return result

if __name__ == "__main__":
    res = part2()
    print(res)
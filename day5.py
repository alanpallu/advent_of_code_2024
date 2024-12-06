
def part1():
    with open("files/day5.txt") as f:
        data = [line.strip() for line in f]

    order = []
    updates = []

    for index in range(len(data)):
        if data[index] == '':
            order = data[:index]
            updates = data[index + 1:]
            break

    order_dict = {}
    for item in order:
        (key, value) = item.split('|')
        if key not in order_dict.keys():
            order_dict[key] = [value]
        else:
            order_dict[key].append(value)

    res = 0
    for row in updates:
        row = row.split(',')
        aux = 0
        for i in range(len(row)):
            remaining = row[:i]
            before_list = order_dict.get(row[i], [])
            matches = [item for item in remaining if item in before_list]
            if len(matches) == 0:
                aux += 1
        if aux == len(row):
            middle_index = len(row)//2
            res += int(row[middle_index])

    return res

def part2():

    with open("files/day5.txt") as f:
        data = [line.strip() for line in f]

    order = []
    updates = []

    for index in range(len(data)):
        if data[index] == '':
            order = data[:index]
            updates = data[index + 1:]
            break

    order_dict = {}
    for item in order:
        (key, value) = item.split('|')
        if key not in order_dict.keys():
            order_dict[key] = [value]
        else:
            order_dict[key].append(value)

    res = 0
    for row in updates:
        row = row.split(',')
        aux = 0
        for i in range(len(row)):
            remaining = row[:i]
            before_list = order_dict.get(row[i], [])
            matches = [item for item in remaining if item in before_list]
            if len(matches) != 0:
                for mat in matches:
                    index = row.index(mat)
                    item = row.pop(index)
                    row.insert(i, item)

            else:
                aux += 1

        if aux != len(row):
            middle_index = len(row) // 2
            res += int(row[middle_index])

    return res

if __name__ == "__main__":
    res1 = part1()
    res2 = part2()
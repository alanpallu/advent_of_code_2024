

def main():
    with open("files/day1.txt") as f:
        list = f.readlines()

    left_list = [int(item.split("   ")[0].strip()) for item in list]
    right_list = [int(item.split("   ")[1].strip()) for item in list]

    left_list.sort()
    right_list.sort()

    res_list = [a_i - b_i for a_i, b_i in zip(left_list, right_list)]
    res_list = [abs(item) for item in res_list]
    result1 = sum(res_list)

    result2 = 0
    for item in left_list:
        count = right_list.count(item)
        result2 += count * item

    return result1, result2

if __name__ == '__main__':
    main()
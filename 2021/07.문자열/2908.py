def get_reversed_int(num):
    return int(str(num)[::-1])


def get_bigger_num(n1, n2):
    return n1 if n1 >= n2 else n2


if __name__ == '__main__':
    num_1, num_2 = input().split()
    print(get_bigger_num(get_reversed_int(num_1), get_reversed_int(num_2)))

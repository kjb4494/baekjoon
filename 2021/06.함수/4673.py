def get_d(n):
    return n + sum([int(str_n) for str_n in str(n)])


if __name__ == '__main__':
    self_number_table = [False] + [True for _ in range(10000)]
    for i in range(10000):
        d = get_d(i)
        if d <= 10000:
            self_number_table[d] = False
    for index, is_self_number in enumerate(self_number_table):
        if is_self_number:
            print(index)

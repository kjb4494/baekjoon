# 분모: 1, / 2, 1, / 1, 2, 3, / 4, 3, 2, 1, / 1, 2, 3, 4, 5, ...
# 분자: 1, / 1, 2, / 3, 2, 1, / 1, 2, 3, 4, / 5, 4, 3, 2, 1, ...

def get_cycle_and_remainder(num):
    cycle = 1
    max_num_in_cycle = 1
    while True:
        if max_num_in_cycle >= num:
            remainder = max_num_in_cycle - num
            return cycle, remainder
        cycle += 1
        max_num_in_cycle += cycle


# 분자
def get_numerator(cycle, remainder):
    if cycle % 2 == 0:
        return cycle - remainder
    else:
        return remainder + 1


# 분모
def get_denominator(cycle, remainder):
    if cycle % 2 == 0:
        return remainder + 1
    else:
        return cycle - remainder


if __name__ == '__main__':
    c, r = get_cycle_and_remainder(int(input()))
    print('{numerator}/{denominator}'.format(
        numerator=get_numerator(c, r),
        denominator=get_denominator(c, r))
    )

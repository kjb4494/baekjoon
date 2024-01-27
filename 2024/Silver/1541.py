# https://www.acmicpc.net/problem/1541
# 잃어버린 괄호


if __name__ == '__main__':
    S = input()
    calc = [[]]
    current_num_str = ""
    for c in S:
        if c == '-':
            calc[-1].append(int(current_num_str))
            calc.append([])
            current_num_str = ""
        elif c == '+':
            calc[-1].append(int(current_num_str))
            current_num_str = ""
        else:
            current_num_str += c
    calc[-1].append(int(current_num_str))

    result = sum(calc[0])
    for i in range(1, len(calc)):
        result -= sum(calc[i])
    print(result)

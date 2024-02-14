# https://www.acmicpc.net/problem/1100
# 하얀 칸


if __name__ == '__main__':
    A = [input() for _ in range(8)]
    is_white = True
    result = 0
    for row in A:
        is_white = not is_white
        for c in row:
            is_white = not is_white
            if is_white and c == 'F':
                result += 1
    print(result)

# https://www.acmicpc.net/problem/1629
# 곱셈

# c^n 분할 정복 거듭제곱
def fpow(c, n):
    result = 1
    while n:
        if n % 2 != 0:
            result = result * c
        c = c * c
        n = n // 2
    return result


def solve(a, b, c):
    if b == 1:
        return a % c

    prev_tmp = solve(a, b//2, c)
    tmp = prev_tmp * prev_tmp % c

    if b % 2 == 1:
        return tmp * a % c
    else:
        return tmp


if __name__ == '__main__':
    A, B, C = list(map(int, input().split()))
    print(solve(A, B, C))

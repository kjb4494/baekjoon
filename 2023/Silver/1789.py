# https://www.acmicpc.net/problem/1789
# 수들의 합

if __name__ == '__main__':
    S = int(input())
    N = 1
    current_sum = 0

    while current_sum + N <= S:
        current_sum += N
        N += 1

    print(N - 1)

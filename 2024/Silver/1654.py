# https://www.acmicpc.net/problem/1654
# 랜선 자르기


import sys


input = sys.stdin.readline


def solve():
    start, end = 1, max(A)
    while start <= end:
        mid = (start + end) // 2
        count = sum(cable // mid for cable in A)

        if count >= N:
            start = mid + 1
        else:
            end = mid - 1
    return end


if __name__ == '__main__':
    K, N = list(map(int, input().split()))
    A = [int(input()) for _ in range(K)]
    print(solve())

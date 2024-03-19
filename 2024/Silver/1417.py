# https://www.acmicpc.net/problem/1417
# 국회의원 선거

import sys

input = sys.stdin.readline


def solve():
    if len(A) == 1:
        return 0

    result = 0
    num_1 = A[0]
    others = sorted(A[1:], reverse=True)
    while True:
        if num_1 > others[0]:
            return result
        result += 1
        num_1 += 1
        others[0] -= 1
        others.sort(reverse=True)


if __name__ == '__main__':
    N = int(input())
    A = [int(input()) for _ in range(N)]
    print(solve())

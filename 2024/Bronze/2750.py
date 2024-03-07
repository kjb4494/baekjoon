# https://www.acmicpc.net/problem/2750
# 수 정렬하기

import sys

input = sys.stdin.readline


if __name__ == '__main__':
    N = int(input())
    A = [int(input()) for _ in range(N)]
    results = sorted(A)

    for result in results:
        print(result)

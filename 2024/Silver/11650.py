# https://www.acmicpc.net/problem/11650
# 좌표 정렬하기

import sys

input = sys.stdin.readline


if __name__ == '__main__':
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    A.sort()
    for x, y in A:
        print(x, y)

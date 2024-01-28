# https://www.acmicpc.net/problem/2751
# 수 정렬하기 2

import sys

input = sys.stdin.readline


if __name__ == '__main__':
    N = int(input())
    A = [int(input()) for _ in range(N)]
    A.sort()
    for num in A:
        print(num)

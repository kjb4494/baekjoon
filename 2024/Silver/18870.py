# https://www.acmicpc.net/problem/18870
# 좌표 압축

import sys

input = sys.stdin.readline


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    coordinate = {num: idx for idx, num in enumerate(sorted(set(A)))}
    print(" ".join([str(coordinate.get(num)) for num in A]))

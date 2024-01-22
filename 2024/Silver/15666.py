# https://www.acmicpc.net/problem/15666
# N과 M (12)

import sys
from itertools import combinations_with_replacement

input = sys.stdin.readline

if __name__ == '__main__':
    N, M = list(map(int, input().split()))
    A = list(set(map(int, input().split())))
    A.sort()

    for comb in combinations_with_replacement(A, M):
        print(" ".join(map(str, comb)))

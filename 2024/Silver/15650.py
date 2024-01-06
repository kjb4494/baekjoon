# https://www.acmicpc.net/problem/15650
# N과 M (2)

from itertools import combinations


def solve():
    for comb in combinations(range(1, N + 1), M):
        print(' '.join(map(str, comb)))


if __name__ == '__main__':
    N, M = list(map(int, input().split()))
    solve()

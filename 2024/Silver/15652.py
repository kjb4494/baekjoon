# https://www.acmicpc.net/problem/15652
# N과 M

from itertools import combinations_with_replacement

if __name__ == '__main__':
    N, M = list(map(int, input().split()))

    for sequence in combinations_with_replacement(range(1, N + 1), M):
        print(" ".join(map(str, sequence)))

# https://www.acmicpc.net/problem/15657
# N과 M (8)

from itertools import combinations_with_replacement

if __name__ == '__main__':
    N, M = list(map(int, input().split()))
    A = list(map(int, input().split()))
    A.sort()

    for comb in combinations_with_replacement(A, M):
        print(" ".join(map(str, comb)))

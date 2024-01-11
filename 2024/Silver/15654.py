# https://www.acmicpc.net/problem/15654
# N과 M (5)

from itertools import permutations

if __name__ == '__main__':
    N, M = list(map(int, input().split()))
    A = list(map(int, input().split()))
    A.sort()

    for comb in permutations(A, M):
        print(' '.join(map(str, comb)))

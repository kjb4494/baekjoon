# https://www.acmicpc.net/problem/15663
# N과 M (9)

from itertools import permutations
import sys

input = sys.stdin.readline

if __name__ == '__main__':
    N, M = list(map(int, input().split()))
    A = list(map(int, input().split()))
    results = []

    for comb in permutations(A, M):
        results.append(comb)

    sorted_results = sorted(set(results))
    for result in sorted_results:
        print(' '.join(map(str, result)))

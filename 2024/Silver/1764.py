# https://www.acmicpc.net/problem/1764
# 듣보잡

import sys

input = sys.stdin.readline

if __name__ == '__main__':
    N, M = list(map(int, input().split()))
    DJ_LIST = {input().strip(): True for _ in range(N)}

    results = []
    for _ in range(M):
        bj = input().strip()
        if DJ_LIST.get(bj):
            results.append(bj)
    results.sort()
    print(len(results))
    for result in results:
        print(result)

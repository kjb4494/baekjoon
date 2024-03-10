# https://www.acmicpc.net/problem/11651
# 좌표 정렬하기 2

import sys

input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    results = []
    for _ in range(N):
        x, y = list(map(int, input().split()))
        results.append((x, y))
    results.sort(key=lambda num_set: (num_set[1], num_set[0]))
    for result in results:
        print(result[0], result[1])

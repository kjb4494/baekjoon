# https://www.acmicpc.net/problem/17219
# 비밀번호 찾기

import sys

input = sys.stdin.readline


if __name__ == '__main__':
    N, M = list(map(int, input().split()))
    MAP = {}
    RESULTS = []
    for _ in range(N):
        domain, password = input().split()
        MAP[domain] = password
    for _ in range(M):
        RESULTS.append(MAP.get(input().strip()))

    for result in RESULTS:
        print(result)

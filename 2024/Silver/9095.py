# https://www.acmicpc.net/problem/9095
# 1, 2, 3 더하기

import sys

input = sys.stdin.readline


def solve(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4

    dp = [0] * (n + 1)
    # 1
    dp[1] = 1
    # 1+1, 2
    dp[2] = 2
    # 1+1+1, 1+2, 2+1, 3
    dp[3] = 4
    for i in range(4, n+1):
        dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
    return dp[-1]


if __name__ == '__main__':
    T = int(input())
    NS = [int(input()) for _ in range(T)]
    for N in NS:
        print(solve(N))

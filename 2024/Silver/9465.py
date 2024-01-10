# https://www.acmicpc.net/problem/9465
# 스티커

import sys

input = sys.stdin.readline


def solve(n, stickers):
    dp = [[0] * n for _ in range(2)]

    dp[0][0] = stickers[0][0]
    dp[1][0] = stickers[1][0]
    if n == 1:
        return max(dp[0][0], dp[1][0])

    dp[0][1] = stickers[1][0] + stickers[0][1]
    dp[1][1] = stickers[0][0] + stickers[1][1]
    if n == 2:
        return max(dp[0][1], dp[1][1])

    for i in range(2, n):
        dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + stickers[0][i]
        dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + stickers[1][i]

    return max(dp[0][n-1], dp[1][n-1])


if __name__ == '__main__':
    T = int(input())
    results = []
    for _ in range(T):
        N = int(input())
        A = [list(map(int, input().split())) for _ in range(2)]
        results.append(solve(N, A))

    for result in results:
        print(result)

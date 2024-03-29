# https://www.acmicpc.net/problem/1912
# 연속합

import sys

input = sys.stdin.readline


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))

    dp = [0] * N
    dp[0] = A[0]
    for i in range(1, N):
        dp[i] = max(dp[i-1] + A[i], A[i])

    print(max(dp))

# https://www.acmicpc.net/problem/2096
# 내려가기

import sys


input = sys.stdin.readline


def solve():
    max_dp = list(map(int, input().split()))
    min_dp = max_dp.copy()

    for i in range(1, N):
        A = list(map(int, input().split()))
        new_max_dp = [0] * 3
        new_min_dp = [0] * 3

        # Calculate max and min for each position
        for j in range(3):
            if j == 0:
                new_max_dp[j] = A[j] + max(max_dp[0], max_dp[1])
                new_min_dp[j] = A[j] + min(min_dp[0], min_dp[1])
            elif j == 2:
                new_max_dp[j] = A[j] + max(max_dp[2], max_dp[1])
                new_min_dp[j] = A[j] + min(min_dp[2], min_dp[1])
            else:
                new_max_dp[j] = A[j] + max(max_dp)
                new_min_dp[j] = A[j] + min(min_dp)

        max_dp, min_dp = new_max_dp, new_min_dp

    print(max(max_dp), min(min_dp))


if __name__ == '__main__':
    N = int(input())
    solve()

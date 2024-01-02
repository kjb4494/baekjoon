# https://www.acmicpc.net/problem/2579
# 계단 오르기


def solve():
    if N == 1:
        return A[0]

    dp = [0] * N
    dp[0] = A[0]

    if N > 1:
        dp[1] = A[0] + A[1]

    if N > 2:
        dp[2] = max(A[0] + A[2], A[1] + A[2])

    for i in range(3, N):
        dp[i] = max(dp[i-2] + A[i], dp[i-3] + A[i-1] + A[i])

    return dp[-1]


if __name__ == '__main__':
    N = int(input())
    A = [int(input()) for _ in range(N)]
    print(solve())

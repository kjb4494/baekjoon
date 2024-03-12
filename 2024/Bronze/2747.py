# https://www.acmicpc.net/problem/2747
# 피보나치 수

def solve():
    if N == 1:
        return 1

    dp = [0] * (N + 1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, N + 1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[-1]


if __name__ == '__main__':
    N = int(input())
    print(solve())

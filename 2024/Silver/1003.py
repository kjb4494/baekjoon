# https://www.acmicpc.net/problem/1003
# 피보나치 함수

if __name__ == '__main__':
    T = int(input())
    N = [int(input()) for _ in range(T)]

    dp = [[0] * 41 for _ in range(2)]
    dp[0][0] = 1
    dp[0][1] = 0
    dp[1][0] = 0
    dp[1][1] = 1

    for i in range(2, 41):
        dp[0][i] = dp[0][i-2] + dp[0][i-1]
        dp[1][i] = dp[1][i-2] + dp[1][i-1]

    for n in N:
        print(dp[0][n], dp[1][n])

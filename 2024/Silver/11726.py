# https://www.acmicpc.net/problem/11726
# 2xn 타일링

if __name__ == '__main__':
    N = int(input())

    dp = [0] * 1000
    dp[0] = 1
    dp[1] = 2

    for i in range(2, 1000):
        dp[i] = (dp[i-2] + dp[i-1]) % 10007

    print(dp[N-1])

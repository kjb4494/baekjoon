# https://www.acmicpc.net/problem/11727
# 2xn 타일링 2

def solve():
    dp = [0] * 1002
    dp[1] = 1
    dp[2] = 3

    for i in range(3, 1002):
        dp[i] = (dp[i-1] + (2 * dp[i-2])) % 10007

    return dp[N]


if __name__ == '__main__':
    N = int(input())
    print(solve())

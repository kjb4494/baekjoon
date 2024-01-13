# https://www.acmicpc.net/problem/9251
# LCS

if __name__ == '__main__':
    FIRST_S = input()
    SECOND_S = input()

    n = len(FIRST_S)
    m = len(SECOND_S)

    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if FIRST_S[i-1] == SECOND_S[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    print(dp)
    print(dp[-1][-1])

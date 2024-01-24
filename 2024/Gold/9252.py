# https://www.acmicpc.net/problem/9252
# LCS2

import sys

input = sys.stdin.readline

if __name__ == '__main__':
    FIRST_S = input().strip()
    SECOND_S = input().strip()
    n = len(FIRST_S)
    m = len(SECOND_S)

    # dp 테이블 & lcs 길이 구하기
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if FIRST_S[i-1] == SECOND_S[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    result_len = dp[-1][-1]
    print(result_len)

    # --- 여기까진 LCS1과 동일함 ---

    # 역추적으로 lcs 구하기
    if result_len > 0:
        lcs = [''] * result_len
        i, j = n, m

        while i > 0 and j > 0:
            if FIRST_S[i-1] == SECOND_S[j-1]:
                lcs[result_len-1] = FIRST_S[i-1]
                i -= 1
                j -= 1
                result_len -= 1
            elif dp[i-1][j] > dp[i][j-1]:
                i -= 1
            else:
                j -= 1
        print(''.join(lcs))

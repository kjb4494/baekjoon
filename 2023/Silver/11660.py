# https://www.acmicpc.net/problem/11660
# 구간 합 구하기 5

import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    N, M = map(int, input().split())
    array = [list(map(int, input().split())) for _ in range(N)]

    # 누적 합 계산
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            dp[i][j] = array[i - 1][j - 1] + dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]

    results = []
    # 쿼리 처리
    for _ in range(M):
        x1, y1, x2, y2 = map(int, input().split())
        answer = dp[x2][y2]
        if x1 > 1: answer -= dp[x1 - 1][y2]
        if y1 > 1: answer -= dp[x2][y1 - 1]
        if x1 > 1 and y1 > 1: answer += dp[x1 - 1][y1 - 1]
        results.append(answer)

    for result in results:
        print(result)

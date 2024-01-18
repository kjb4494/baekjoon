# https://www.acmicpc.net/problem/17404
# RGB거리 2

import sys

input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    result = float('inf')

    # 첫번째 집을 무슨 색으로 칠할지 경우의 수 반복문
    for i in range(3):
        # dp element: [R, G, B]
        dp = [[float('inf'), float('inf'), float('inf')] for _ in range(N)]

        # 첫 집 색칠
        dp[0][i] = A[0][i]

        # 두번째 집부터 R, G, B로 색칠했을 때 최소값 dp 채우기
        for j in range(1, N):
            dp[j][0] = A[j][0] + min(dp[j - 1][1], dp[j - 1][2])
            dp[j][1] = A[j][1] + min(dp[j - 1][0], dp[j - 1][2])
            dp[j][2] = A[j][2] + min(dp[j - 1][0], dp[j - 1][1])

        # 첫번째 집과 N번째 집의 색이 다른 경우만 선택
        for k in range(3):
            if i != k:
                result = min(result, dp[-1][k])
    print(result)

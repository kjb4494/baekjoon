# https://www.acmicpc.net/problem/1010

import math


# 조합을 이용한 풀이
def solve(n, m):
    if 0 <= n <= m:
        return math.factorial(m) // (math.factorial(n) * math.factorial(m - n))
    else:
        return 0


# 다이나믹 프로그래밍을 이용한 풀이
def solve_2(n, m):
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(m + 1):
        dp[1][i] = i

    for i in range(2, n + 1):
        for j in range(i, m + 1):
            dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1]

    return dp[n][m]


if __name__ == '__main__':
    T = int(input())
    result_list = []
    for tc in range(T):
        N, M = map(int, input().split())
        result_list.append(solve(N, M))
    print("\n".join(map(str, result_list)))

# https://www.acmicpc.net/problem/1932
# 정수 삼각형


def solve():
    if N == 1:
        return A[0][0]

    dp = [[0 for _ in i] for i in A]
    dp[0][0] = A[0][0]
    for i in range(1, len(A)):
        for j in range(len(A[i])):
            if j == 0:
                dp[i][j] = A[i][j] + dp[i-1][j]
            elif j == len(A[i]) - 1:
                dp[i][j] = A[i][j] + dp[i-1][-1]
            else:
                dp[i][j] = A[i][j] + max(dp[i-1][j-1], dp[i-1][j])
    return max(dp[-1])


if __name__ == '__main__':
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    print(solve())

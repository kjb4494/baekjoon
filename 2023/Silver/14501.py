# https://www.acmicpc.net/problem/14501
# 퇴사

if __name__ == '__main__':
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]

    dp = [0 for i in range(N+1)]

    for i in range(N):
        for j in range(i+A[i][0], N+1):
            if dp[j] < dp[i] + A[i][1]:
                dp[j] = dp[i] + A[i][1]

    print(dp[-1])

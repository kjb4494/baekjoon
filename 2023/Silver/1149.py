# https://www.acmicpc.net/problem/1149
# RGB 거리

if __name__ == '__main__':
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]

    for i in range(1, N):
        A[i][0] += min(A[i-1][1], A[i-1][2])
        A[i][1] += min(A[i-1][0], A[i-1][2])
        A[i][2] += min(A[i-1][0], A[i-1][1])

    print(min(A[N-1]))

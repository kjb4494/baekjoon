# https://www.acmicpc.net/problem/18111
# 마인크래프트

import sys

input = sys.stdin.readline


def solve():
    min_time = float('inf')
    result_height = -1

    for height in range(257):
        build = 0
        remove = 0

        for i in range(N):
            for j in range(M):
                if A[i][j] < height:
                    build += height - A[i][j]
                else:
                    remove += A[i][j] - height

        if build <= remove + B:
            time = build + remove * 2
            if time <= min_time:
                min_time = time
                result_height = height

    return min_time, result_height


if __name__ == '__main__':
    N, M, B = list(map(int, input().split()))
    A = [list(map(int, input().split())) for _ in range(N)]
    t, h = solve()
    print(t, h)

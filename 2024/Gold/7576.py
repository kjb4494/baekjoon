# https://www.acmicpc.net/problem/7576
# 토마토

from collections import deque
import sys


input = sys.stdin.readline


def bfs(grid, start_points):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    queue = deque(start_points)
    # 모든 토마토가 이미 익어있는 경우를 고려
    days = -1

    while queue:
        days += 1
        for _ in range(len(queue)):
            i, j = queue.popleft()
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < M and grid[ni][nj] == 0:
                    grid[ni][nj] = 1
                    queue.append((ni, nj))

    # 모든 토마토가 익었는지 확인
    for row in grid:
        if 0 in row:
            return -1
    return days


def solve():
    tomato_box = A
    start_points = [(i, j) for i in range(N) for j in range(M) if tomato_box[i][j] == 1]
    return bfs(tomato_box, start_points)


if __name__ == '__main__':
    M, N = list(map(int, input().split()))
    A = [list(map(int, input().split())) for _ in range(N)]
    print(solve())

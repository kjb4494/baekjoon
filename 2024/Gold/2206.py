# https://www.acmicpc.net/problem/2206
# 벽 부수고 이동하기

import sys
from collections import deque

input = sys.stdin.readline


def bfs():
    # 방문 기록: [x][y][벽 부순 횟수]
    visited = [[[False] * 2 for _ in range(M)] for _ in range(N)]
    # x, y, 이동 거리, 벽 부순 횟수
    queue = deque([(0, 0, 1, 0)])
    visited[0][0][0] = True

    while queue:
        x, y, dist, break_wall = queue.popleft()

        # 도착
        if x == N - 1 and y == M - 1:
            return dist

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < M:
                # 벽 있는데 아직 안 부쉈을 때
                if A[nx][ny] == 1 and break_wall == 0 and not visited[nx][ny][1]:
                    visited[nx][ny][1] = True
                    queue.append((nx, ny, dist + 1, 1))

                # 벽 없을 때
                elif A[nx][ny] == 0 and not visited[nx][ny][break_wall]:
                    visited[nx][ny][break_wall] = True
                    queue.append((nx, ny, dist + 1, break_wall))

    # 도달 불가능
    return -1


if __name__ == '__main__':
    N, M = list(map(int, input().split()))
    A = [list(map(int, list(input().strip()))) for _ in range(N)]
    print(bfs())

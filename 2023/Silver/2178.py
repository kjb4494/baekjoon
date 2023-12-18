# https://www.acmicpc.net/problem/2178
# 미로 탐색
# BFS 문제

from collections import deque


def solve(maze, n, m):
    # 방향 벡터 (상, 하, 좌, 우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # BFS를 위한 큐
    queue = deque()
    queue.append((0, 0))  # 시작 위치 (0, 0)에서 시작

    while queue:
        x, y = queue.popleft()

        # 현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로 범위를 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 벽인 경우 무시
            if maze[nx][ny] == 0:
                continue

            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))

    # 마지막 노드까지의 최단 거리 반환
    return maze[n - 1][m - 1]


if __name__ == '__main__':
    N, M = list(map(int, input().split()))
    A = [[int(i) for i in input()] for _ in range(N)]
    print(solve(A, N, M))

# https://www.acmicpc.net/problem/2667
# 단지번호붙이기
# BFS 문제

def bfs(start):
    d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    queue = [start]
    VISITED[start[0]][start[1]] = True
    count = 1

    while queue:
        x, y = queue.pop(0)
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and not VISITED[nx][ny] and A[nx][ny] == 1:
                queue.append((nx, ny))
                VISITED[nx][ny] = True
                count += 1

    return count


if __name__ == '__main__':
    N = int(input())
    A = [[int(i) for i in input()] for _ in range(N)]
    VISITED = [[False] * N for _ in range(N)]

    result = []
    for i in range(N):
        for j in range(N):
            if not VISITED[i][j] and A[i][j] == 1:
                result.append(bfs((i, j)))

    print(len(result))
    for c in sorted(result):
        print(c)

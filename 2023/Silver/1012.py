# https://www.acmicpc.net/problem/1012
# 유기농 배추

def bfs(visited, ground, n, m, start):
    d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    queue = [start]
    visited[start[0]][start[1]] = True
    count = 1
    while queue:
        x, y = queue.pop(0)
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and ground[nx][ny] == 1:
                queue.append((nx, ny))
                visited[nx][ny] = True
                count += 1
    return count


def get_result_count():
    m, n, k = list(map(int, input().split()))
    ground = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]
    result = []
    for _ in range(k):
        [i, j] = list(map(int, input().split()))
        ground[j][i] = 1
    for i in range(n):
        for j in range(m):
            if ground[i][j] == 1 and not visited[i][j]:
                result.append(bfs(visited, ground, n, m, (i, j)))
    return len(result)


if __name__ == '__main__':
    T = int(input())
    result_counts = [get_result_count() for _ in range(T)]
    for result_count in result_counts:
        print(result_count)

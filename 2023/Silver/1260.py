# https://www.acmicpc.net/problem/1260
# DFS와 BFS

from collections import deque


def dfs(graph, start_node):
    visited = set()
    stack = [start_node]
    result = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            result.append(node)
            stack += sorted(graph[node] - visited, reverse=True)

    return result


def bfs(graph, start_node):
    visited = set()
    queue = deque([start_node])
    result = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            result.append(node)
            queue += sorted(graph[node] - visited)

    return result


if __name__ == '__main__':
    # 입력
    N, M, V = map(int, input().split())
    graph = {i: set() for i in range(1, N+1)}

    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].add(b)
        graph[b].add(a)

    # DFS와 BFS 수행
    dfs_result = dfs(graph, V)
    bfs_result = bfs(graph, V)

    # 출력
    print(*dfs_result)
    print(*bfs_result)

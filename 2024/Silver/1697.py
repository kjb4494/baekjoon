# https://www.acmicpc.net/problem/1697
# 숨바꼭질

from collections import deque


def solve():
    visited = [-1] * 200000
    queue = deque([N])
    visited[N] = 0

    while queue:
        current_node = queue.popleft()
        if current_node == K:
            return visited[current_node]
        next_nodes = [current_node - 1, current_node + 1, current_node * 2]
        for next_node in next_nodes:
            if 0 <= next_node < len(visited) and visited[next_node] == -1:
                queue.append(next_node)
                visited[next_node] = visited[current_node] + 1


if __name__ == '__main__':
    N, K = list(map(int, input().split()))
    print(solve())

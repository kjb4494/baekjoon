# https://www.acmicpc.net/problem/11724
# 연결 요소의 개수

from collections import deque
import sys

input = sys.stdin.readline


def make_graph():
    graph = {i: set() for i in range(N)}
    for _ in range(M):
        i, j = list(map(int, input().split()))
        graph[i - 1].add(j - 1)
        graph[j - 1].add(i - 1)
    return graph


def bfs(graph, visited, start_node_index):
    queue = deque([start_node_index])
    visited[start_node_index] = True

    while queue:
        current_node_index = queue.popleft()
        for node_index in graph[current_node_index]:
            if not visited[node_index]:
                visited[node_index] = True
                queue.append(node_index)


def solve():
    graph = make_graph()
    visited = [False] * N
    connected_component = 0
    for i in range(N):
        if not visited[i]:
            bfs(graph, visited, i)
            connected_component += 1
    return connected_component


if __name__ == '__main__':
    N, M = list(map(int, input().split()))
    print(solve())

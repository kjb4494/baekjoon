# https://www.acmicpc.net/problem/1167
# 트리의 지름

from collections import deque
import sys

input = sys.stdin.readline


def bfs(graph, start):
    visited = [-1] * (len(graph) + 1)
    queue = deque([start])
    visited[start] = 0
    farthest_node = 0
    max_distance = 0

    while queue:
        current_node = queue.popleft()
        for next_node, distance in graph[current_node]:
            if visited[next_node] == -1:
                visited[next_node] = visited[current_node] + distance
                queue.append(next_node)
                if visited[next_node] > max_distance:
                    farthest_node = next_node
                    max_distance = visited[next_node]

    return farthest_node, max_distance


def solve():
    graph = [[] for _ in range(V + 1)]
    for edge in EDGES:
        graph[edge[0]].append((edge[1], edge[2]))
        graph[edge[1]].append((edge[0], edge[2]))
    farthest_node, _ = bfs(graph, 1)
    _, diameter = bfs(graph, farthest_node)

    return diameter


if __name__ == '__main__':
    V = int(input())
    EDGES = []
    for _ in range(V):
        nums = list(map(int, input().split()))
        for i in range(1, len(nums) - 1, 2):
            EDGES.append((nums[0], nums[i], nums[i + 1]))
    print(solve())

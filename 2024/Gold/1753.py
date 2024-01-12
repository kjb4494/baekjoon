# https://www.acmicpc.net/problem/1753
# 최단경로

import heapq
import sys

input = sys.stdin.readline


# 처음에 bfs처럼 deque로 해봤는데 시간복잡도에서 실패함
def dijkstra():
    distances = {node: float('inf') for node in GRAPH}
    distances[START_NODE_INDEX] = 0
    queue = [(0, START_NODE_INDEX)]

    while queue:
        current_distance, current_node_index = heapq.heappop(queue)

        if distances[current_node_index] < current_distance:
            continue

        for next_node_index, distance_to_next_node in GRAPH[current_node_index]:
            distance = current_distance + distance_to_next_node
            if distance < distances[next_node_index]:
                distances[next_node_index] = distance
                heapq.heappush(queue, (distance, next_node_index))

    return distances


if __name__ == '__main__':
    V, E = list(map(int, input().split()))
    START_NODE_INDEX = int(input())
    GRAPH = {i: set() for i in range(1, V + 1)}
    for _ in range(E):
        u, v, w = list(map(int, input().split()))
        GRAPH[u].add((v, w))

    DISTANCES = dijkstra()
    for i in range(1, V + 1):
        print(DISTANCES[i] if DISTANCES[i] != float('inf') else "INF")

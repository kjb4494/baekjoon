# https://www.acmicpc.net/problem/1916
# 최소비용 구하기

import heapq
import sys

input = sys.stdin.readline


def dijkstra():
    costs = {node: float('inf') for node in GRAPH}
    costs[START_NODE_INDEX] = 0

    # cost, node_index
    queue = [(0, START_NODE_INDEX)]

    while queue:
        current_cost, current_node_index = heapq.heappop(queue)

        if costs[current_node_index] < current_cost:
            continue

        for next_node_index, cost_to_next_node in GRAPH[current_node_index]:
            cost = current_cost + cost_to_next_node
            if cost < costs[next_node_index]:
                costs[next_node_index] = cost
                heapq.heappush(queue, (cost, next_node_index))

    return costs


if __name__ == '__main__':
    N = int(input())
    M = int(input())
    GRAPH = {i: set() for i in range(1, N + 1)}
    for _ in range(M):
        # 출발 도시 번호, 도착지 도시 번호, 버스 비용
        u, v, w = list(map(int, input().split()))
        GRAPH[u].add((v, w))
    START_NODE_INDEX, DESTINATION_NODE_INDEX = list(map(int, input().split()))
    COSTS = dijkstra()
    print(COSTS[DESTINATION_NODE_INDEX])

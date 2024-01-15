# https://www.acmicpc.net/problem/11725
# 트리의 부모 찾기
import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def dfs(node, prev):
    PARENT[node] = prev
    for child in TREE[node]:
        if child != prev:
            dfs(child, node)


if __name__ == '__main__':
    N = int(input())
    TREE = {i: set() for i in range(1, N + 1)}
    for _ in range(N - 1):
        node1, node2 = list(map(int, input().split()))
        TREE[node1].add(node2)
        TREE[node2].add(node1)
    PARENT = [0] * (N + 1)
    dfs(1, 0)

    for i in range(2, N + 1):
        print(PARENT[i])

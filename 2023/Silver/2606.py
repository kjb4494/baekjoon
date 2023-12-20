# https://www.acmicpc.net/problem/2606
# 바이러스

if __name__ == '__main__':
    N = int(input())
    M = int(input())
    A = [list(map(int, input().split())) for _ in range(M)]

    graph = {i: set() for i in range(1, N+1)}

    for a in A:
        graph[a[0]].add(a[1])
        graph[a[1]].add(a[0])

    visited = set()
    stack = [1]
    result = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            result.append(node)
            stack += sorted(graph[node] - visited, reverse=True)
            print(stack)

    print(len(result) - 1)

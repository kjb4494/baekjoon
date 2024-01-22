# https://www.acmicpc.net/problem/13549
# 숨바꼭질 3

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
                if next_node == current_node * 2:
                    # 순간이동은 0 코스트라서 큐의 제일 앞쪽으로 넣어 우선순위를 높혀준다.
                    # 이 부분이 숨바꼭질 1 문제와의 차이점!
                    queue.appendleft(next_node)
                    visited[next_node] = visited[current_node]
                else:
                    queue.append(next_node)
                    visited[next_node] = visited[current_node] + 1


if __name__ == '__main__':
    N, K = list(map(int, input().split()))
    print(solve())

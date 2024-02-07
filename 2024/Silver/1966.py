# https://www.acmicpc.net/problem/1966
# 프린터 큐

import sys
from collections import deque

input = sys.stdin.readline

if __name__ == '__main__':
    results = []

    T = int(input())
    for _ in range(T):
        N, M = list(map(int, input().split()))
        A = list(map(int, input().split()))

        queue = deque([(value, idx) for idx, value in enumerate(A)])
        print_order = 0
        while queue:
            current = queue.popleft()
            if any(current[0] < other[0] for other in queue):
                queue.append(current)
            else:
                print_order += 1
                if current[1] == M:
                    results.append(print_order)

    for result in results:
        print(result)

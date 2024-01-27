# https://www.acmicpc.net/problem/11279
# 최대 힙

import heapq
import sys

input = sys.stdin.readline


if __name__ == '__main__':
    N = int(input())
    A = [int(input()) for _ in range(N)]

    queue = []
    for num in A:
        if num == 0:
            print(-heapq.heappop(queue) if queue else 0)
        else:
            heapq.heappush(queue, -num)

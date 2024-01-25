# https://www.acmicpc.net/problem/1927
# 최소 힙

import heapq
import sys

input = sys.stdin.readline


if __name__ == '__main__':
    N = int(input())
    A = [int(input()) for _ in range(N)]

    queue = []
    for num in A:
        if num == 0:
            print(heapq.heappop(queue)) if queue else print(0)
        else:
            heapq.heappush(queue, num)

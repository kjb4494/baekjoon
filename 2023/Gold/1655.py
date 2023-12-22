# https://www.acmicpc.net/problem/1655
# 가운데를 말해요

import heapq
import sys


if __name__ == '__main__':
    input = sys.stdin.readline
    N = int(input())
    max_heap, min_heap = [], []
    results = []

    for _ in range(N):
        num = int(input())

        if len(max_heap) == len(min_heap):
            heapq.heappush(max_heap, (-num, num))
        else:
            heapq.heappush(min_heap, (num, num))

        if min_heap and max_heap[0][1] > min_heap[0][0]:
            max_val = heapq.heappop(max_heap)[1]
            min_val = heapq.heappop(min_heap)[0]
            heapq.heappush(max_heap, (-min_val, min_val))
            heapq.heappush(min_heap, (max_val, max_val))

        results.append(max_heap[0][1])

    for result in results:
        print(result)

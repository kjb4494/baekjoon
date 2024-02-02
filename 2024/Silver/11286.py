# https://www.acmicpc.net/problem/11286
# 절댓값 힙

import heapq
import sys

input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    A = [int(input()) for _ in range(N)]

    queue = []
    for num in A:
        if num == 0:
            if queue:
                abs_num, orig_num = heapq.heappop(queue)
                print(orig_num)
            else:
                print(0)
        else:
            heapq.heappush(queue, (abs(num), num))

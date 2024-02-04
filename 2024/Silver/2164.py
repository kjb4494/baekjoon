# https://www.acmicpc.net/problem/2164
# 카드2

from collections import deque

if __name__ == '__main__':
    N = int(input())
    queue = deque([i for i in range(N, 0, -1)])
    while len(queue) > 1:
        current_num = queue.pop()
        queue.appendleft(queue.pop())
    print(queue.pop())

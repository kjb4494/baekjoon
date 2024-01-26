# https://www.acmicpc.net/problem/1874
# 스택 수열

import sys
from collections import deque


input = sys.stdin.readline

def solve():
    results = []
    stack = []
    for i in range(1, N + 1):
        stack.append(i)
        results.append("+")
        while stack and stack[-1] == A[0]:
            results.append("-")
            stack.pop()
            A.popleft()

    if stack:
        print("NO")
    else:
        for result in results:
            print(result)


if __name__ == '__main__':
    N = int(input())
    A = deque([int(input()) for _ in range(N)])
    solve()

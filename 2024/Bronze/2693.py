# https://www.acmicpc.net/problem/2693
# N번쨰 큰 수

import sys


input = sys.stdin.readline


if __name__ == '__main__':
    T = int(input())
    results = []
    for _ in range(T):
        A = list(map(int, input().split()))
        A.sort(reverse=True)
        results.append(A[2])
    for result in results:
        print(result)

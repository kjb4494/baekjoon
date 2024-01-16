# https://www.acmicpc.net/problem/11659
# 구간 합 구하기 4

import sys

input = sys.stdin.readline

if __name__ == '__main__':
    N, M = list(map(int, input().split()))
    A = list(map(int, input().split()))
    prefix_sum = [0]
    for i in range(len(A)):
        prefix_sum.append(prefix_sum[i] + A[i])
    results = []
    for _ in range(M):
        i, j = list(map(int, input().split()))
        results.append(prefix_sum[j] - prefix_sum[i-1])
    for result in results:
        print(result)

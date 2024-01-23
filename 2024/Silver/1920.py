# https://www.acmicpc.net/problem/1920
# 수 찾기

import sys

input = sys.stdin. readline


def binary_search(num):
    start = 0
    end = len(A) - 1
    while start <= end:
        mid = (start + end) // 2

        if A[mid] == num:
            return 1
        elif A[mid] > num:
            end = mid - 1
        else:
            start = mid + 1
    return 0


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    M = int(input())
    B = list(map(int, input().split()))

    A.sort()
    for b in B:
        print(binary_search(b))

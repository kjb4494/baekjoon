# https://www.acmicpc.net/problem/11728
# 배열 합치기

import sys

input = sys.stdin.readline

if __name__ == '__main__':
    N, M = list(map(int, input().split()))
    result = []
    for i in list(map(int, input().split())):
        result.append(i)
    for i in list(map(int, input().split())):
        result.append(i)
    result.sort()
    print(" ".join(map(str, result)))

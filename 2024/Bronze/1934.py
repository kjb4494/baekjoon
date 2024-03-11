# https://www.acmicpc.net/problem/1934
# 최소공배수

import math
import sys

input = sys.stdin.readline

if __name__ == '__main__':
    T = int(input())
    results = []
    for _ in range(T):
        a, b = list(map(int, input().split()))
        results.append(a * b // math.gcd(a, b))
    for result in results:
        print(result)


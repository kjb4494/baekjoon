# https://www.acmicpc.net/problem/3052
# 나머지

from collections import Counter

if __name__ == '__main__':
    A = [int(input()) % 42 for _ in range(10)]
    print(len(Counter(A)))

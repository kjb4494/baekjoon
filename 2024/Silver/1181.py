# https://www.acmicpc.net/problem/1181
# 단어 정렬

import sys

input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    A = list(set(input().strip() for _ in range(N)))
    A.sort(key=lambda s: (len(s), s))

    for result in A:
        print(result)

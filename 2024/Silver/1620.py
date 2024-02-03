# https://www.acmicpc.net/problem/1620
# 나는야 포켓몬 마스터 이다솜

import sys

input = sys.stdin.readline


if __name__ == '__main__':
    N, M = list(map(int, input().split()))
    A = [input().strip() for _ in range(N)]
    A_map = {value: i + 1 for i, value in enumerate(A)}

    for i in range(M):
        input_str = input().strip()
        try:
            key = int(input_str)
            print(A[key - 1])
        except ValueError:
            print(A_map.get(input_str))

# https://www.acmicpc.net/problem/2408
# 큰 수 계산

import sys

input = sys.stdin.readline


if __name__ == '__main__':
    N = int(input())
    oper_str = ""
    for _ in range(2 * N - 1):
        oper_str += input().strip().replace("/", "//")
    print(eval(oper_str))

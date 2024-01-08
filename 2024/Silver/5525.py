# https://www.acmicpc.net/problem/5525
# IOIOI

import sys

input = sys.stdin.readline


def solve():
    Pn = "I" + "OI" * N
    Pn_size = len(Pn)

    result = 0
    for i in range(0, len(S) - Pn_size + 1):
        if S[i:i+Pn_size] == Pn:
            result += 1

    print(result)


def solve_better():
    count = 0
    index = 0

    while index < len(S):
        if S[index] == 'I':
            OI_count = 0
            index += 1
            while index < len(S) - 1:
                if S[index:index+2] == "OI":
                    OI_count += 1
                    index += 2
                else:
                    break
                if OI_count >= N:
                    count += 1
        else:
            index += 1
    print(count)


if __name__ == '__main__':
    N = int(input())
    M = int(input())
    S = input()
    solve_better()

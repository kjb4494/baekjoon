# https://www.acmicpc.net/problem/8958
# OX퀴즈

import sys

input = sys.stdin.readline


if __name__ == '__main__':
    T = int(input())
    results = []
    for _ in range(T):
        S = input()
        result = 0
        current_score = 0
        for c in S:
            if c == 'O':
                current_score += 1
                result += current_score
            else:
                current_score = 0
        results.append(result)
    for result in results:
        print(result)

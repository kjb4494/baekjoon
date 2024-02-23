# https://www.acmicpc.net/problem/1009
# 분산처리

import sys

input = sys.stdin.readline


def solve(num_a, num_b):
    if num_a == 1:
        return 1
    loop_list = []
    computer_number = 1
    for _ in range(num_b):
        computer_number = (computer_number * num_a) % 10
        if computer_number in loop_list:
            break
        loop_list.append(computer_number)
    computer_number = loop_list[(num_b - 1) % len(loop_list)]
    return computer_number if computer_number != 0 else 10


if __name__ == '__main__':
    T = int(input())
    results = []
    for i in range(T):
        a, b = list(map(int, input().split()))
        results.append(solve(a, b))

    for result in results:
        print(result)

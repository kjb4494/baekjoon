# https://www.acmicpc.net/problem/14888
# 연산자 끼워넣기

from itertools import permutations


def calc(ops):
    result = A[0]
    for i in range(1, N):
        if ops[i-1] == '+':
            result += A[i]
        elif ops[i-1] == '-':
            result -= A[i]
        elif ops[i-1] == '*':
            result *= A[i]
        else:
            if result < 0:
                result = -(-result // A[i])
            else:
                result //= A[i]
    return result


def solve():
    operators = ['+'] * OP[0] + ['-'] * OP[1] + ['*'] * OP[2] + ['/'] * OP[3]
    min_result, max_result = float('inf'), float('-inf')

    for ops in set(permutations(operators, N-1)):
        result = calc(ops)
        min_result = min(min_result, result)
        max_result = max(max_result, result)

    print(max_result)
    print(min_result)


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    OP = list(map(int, input().split()))
    solve()

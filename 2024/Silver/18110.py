# https://www.acmicpc.net/problem/18110
# solved.ac

import sys

input = sys.stdin.readline


# 기존 round 함수는 은행가 반올림 법칙을 사용한다.
# 사사오입 반올림이 필요하기 때문에 직접 구현해야한다.
def solve_round(num):
    if num - int(num) >= 0.5:
        return int(num) + 1
    else:
        return int(num)


def solve():
    if not A:
        return 0

    cutting_count = solve_round(len(A) * 0.15)
    if cutting_count == 0:
        return solve_round(sum(A) / len(A))

    cutting_A = A[cutting_count:-cutting_count]
    return solve_round(sum(cutting_A) / len(cutting_A))


if __name__ == '__main__':
    n = int(input())
    A = [int(input()) for _ in range(n)]
    A.sort()

    print(solve())

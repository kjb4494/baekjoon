# https://www.acmicpc.net/problem/6064
# 카잉 달력

import sys

input = sys.stdin.readline


# 시간초과로 실패했음
def solve(m, n, x, y):
    year = 1
    while year <= m * n:
        search_x = year % m if year % m != 0 else m
        search_y = year % n if year % n != 0 else n

        if search_x == x and search_y == y:
            return year
        year += 1
    return -1


# https://ji-gwang.tistory.com/249
def solve_better(m, n, x, y):
    k = x  # k를 x로 초기화
    while k <= m * n:  # k의 범위는 m*n을 넘을 수 없기에
        if (k - x) % m == 0 and (k - y) % n == 0:  # 2개의 조건을 만족하는 k값을 찾는다.
            return k
        k += m  # k-x가 m의 배수이기 때문에 k는 x로 초기화해주었기 때문에 m만 더해준다.
    return -1


if __name__ == '__main__':
    T = int(input())
    results = []
    for _ in range(T):
        results.append(solve_better(*map(int, input().split())))
    for result in results:
        print(result)

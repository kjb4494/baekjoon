# https://www.acmicpc.net/contest/problem/1206/3
# C번 - 위잉위잉

import math
import sys
from decimal import Decimal, getcontext


# 틀렸다는데 왜 틀렸는지 모르겠음 ㅠㅠ
def solve():
    getcontext().prec = 50
    polar_people = []
    for i, (x, y) in enumerate(people):
        dx, dy = x - hyuk[0], y - hyuk[1]
        # 계산 정밀도 때문에 Decimal 넣어봄
        radians = Decimal(math.atan2(dy, dx))
        # 각도 경계 처리
        if radians == math.pi:
            radians = -radians
        distance = dx ** 2 + dy ** 2
        polar_people.append((radians, distance, x, y))

    polar_people.sort()

    for _, _, x, y in polar_people:
        print(x, y)


if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    people = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
    hyuk = list(map(int, sys.stdin.readline().strip().split()))
    solve()

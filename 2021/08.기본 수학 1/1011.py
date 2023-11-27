# 1     1               1 <-
# 2     11              2 <-
# 3     111             3
# 4     121             3 <-
# 5     1211            4
# 6     1221            4 <-
# 7     12211           5
# 8     12221           5
# 9     12321           5 <-
# 10    123211          6
# 11    123221          6
# 12    123321          6 <-
# 13    1233211         7
# 14    1233221         7
# 15    1233321         7
# 16    1234321         7 <-
# 17    12343211        8
# 18    12343221        8
# ...

# 이동 장치 작동 횟수 변환점
# 1 + 2 + 3 + ... + (n-1) + (n-1) + ... + 3 + 2 + 1 = (n-1)n ... 1
# 1 + 2 + 3 + ... + (n-1) + n + (n-1) + ... + 3 + 2 + 1 = n^2 ... 2

# (y-x)가 1에 가까운지 2에 가까운지 판별
# 1의 경우 (n * 2) - 2
# 2의 경우 (n * 2) - 1

import math


def get_operation_count(location_x, location_y):
    distance = location_y - location_x
    n = math.ceil(distance ** 0.5)
    return n * 2 - 1 if distance > n ** 2 - n else n * 2 - 2


if __name__ == '__main__':
    output = []

    T = int(input())
    for _ in range(T):
        x, y = map(int, input().split())
        output.append(str(get_operation_count(x, y)))

    print('\n'.join(output))

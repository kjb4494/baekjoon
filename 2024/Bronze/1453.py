# https://www.acmicpc.net/problem/1453
# 피시방 알바

def solve():
    seat = [False] * 100
    result = 0
    for seat_num in A:
        if seat[seat_num-1]:
            result += 1
        else:
            seat[seat_num-1] = True
    return result


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))

    print(solve())

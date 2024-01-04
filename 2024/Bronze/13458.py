# https://www.acmicpc.net/problem/13458
# 시험 감독


def solve():
    result = 0
    for i in A:
        # 총 감독관
        result += 1
        if i <= B:
            continue

        # 부 감독관
        remain_i = i - B
        c_count = remain_i // C
        if remain_i % C != 0:
            c_count += 1
        result += c_count
    return result


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    B, C = list(map(int, input().split()))
    print(solve())

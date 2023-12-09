# https://www.acmicpc.net/problem/1037
# 약수

def solve():
    return min(A_LIST) * max(A_LIST)


if __name__ == '__main__':
    N_COUNT = int(input())
    A_LIST = list(map(int, input().split()))
    print(solve())

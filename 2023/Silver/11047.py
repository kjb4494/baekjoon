# https://www.acmicpc.net/problem/11047
# 동전 0

if __name__ == '__main__':
    N, K = list(map(int, input().split()))
    COINS = [int(input()) for _ in range(N)]
    COINS.reverse()

    count = 0
    for coin in COINS:
        count += K // coin
        K = K % coin
    print(count)

# https://www.acmicpc.net/problem/11050
# 이항 계수 1

import math

if __name__ == '__main__':
    N, K = list(map(int, input().split()))
    print(math.factorial(N) // (math.factorial(N - K) * math.factorial(K)))

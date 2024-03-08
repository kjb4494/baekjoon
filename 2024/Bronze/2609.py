# https://www.acmicpc.net/problem/2609
# 최대공약수와 최소공배수

import math

if __name__ == '__main__':
    N, M = list(map(int, input().split()))
    gcd = math.gcd(N, M)
    print(gcd)
    print(N * M // gcd)

# https://www.acmicpc.net/problem/1252
# 이진수 덧셈

if __name__ == '__main__':
    A = list(map(lambda x: int(x, 2), input().split()))
    print(bin(sum(A))[2:])

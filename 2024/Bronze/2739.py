# https://www.acmicpc.net/problem/2739
# 구구단

if __name__ == '__main__':
    N = int(input())
    for i in range(1, 10):
        print("{} * {} = {}".format(N, i, N*i))

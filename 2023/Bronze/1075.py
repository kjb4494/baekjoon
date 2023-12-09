# https://www.acmicpc.net/problem/1075
# 나누기

def solve():
    n_base = (N // 100) * 100
    for i in range(100):
        if (n_base + i) % F == 0:
            return str(i).zfill(2)


if __name__ == '__main__':
    N = int(input())
    F = int(input())
    print(solve())

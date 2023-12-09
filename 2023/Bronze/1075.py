
def solve():
    n_base = (N // 100) * 100
    for i in range(100):
        if (n_base + i) % F == 0:
            return str(i).zfill(2)


if __name__ == '__main__':
    N = int(input())
    F = int(input())
    print(solve())

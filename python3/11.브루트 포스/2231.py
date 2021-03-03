
def decomposition_sum(n):
    return n + sum([int(digits) for digits in str(n)])


if __name__ == '__main__':
    N = int(input())
    for i in range(max(1, N-9*len(str(N))), N):
        if decomposition_sum(i) == N:
            print(i)
            exit()
    print(0)

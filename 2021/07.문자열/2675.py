if __name__ == '__main__':
    repeat = int(input())
    P = []
    for _ in range(repeat):
        count, S = input().split()
        P.append(''.join([int(count) * s for s in S]))
    print('\n'.join(P))

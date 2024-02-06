# https://www.acmicpc.net/problem/10814
# 나이순 정렬

if __name__ == '__main__':
    N = int(input())
    A = []
    for i in range(N):
        year, name = input().split()
        A.append((int(year), i, name))
    A.sort()

    for year, _, name in A:
        print(year, name)

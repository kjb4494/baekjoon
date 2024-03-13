# https://www.acmicpc.net/problem/2587
# 대표값2


if __name__ == '__main__':
    A = [int(input()) for _ in range(5)]
    A.sort()
    print(sum(A) // 5)
    print(A[2])

import sys

input = sys.stdin.readline


if __name__ == '__main__':
    N = int(input())
    A = {int(num): True for num in input().split()}
    M = int(input())
    B = list(map(int, input().split()))

    for b in B:
        print(1 if A.get(b) else 0)

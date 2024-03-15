# https://www.acmicpc.net/problem/7567
# 그릇

if __name__ == '__main__':
    A = list(input())
    result = 10
    for i in range(1, len(A)):
        if A[i-1] == A[i]:
            result += 5
        else:
            result += 10
    print(result)

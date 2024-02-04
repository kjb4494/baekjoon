# https://www.acmicpc.net/problem/1676
# 팩토리얼 0의 개수

if __name__ == '__main__':
    N = int(input())

    num = 1
    result = 0
    for i in range(2, N+1):
        num *= i
        while num % 10 == 0:
            num //= 10
            result += 1
    print(result)

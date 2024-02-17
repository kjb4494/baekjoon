# https://www.acmicpc.net/problem/1145
# 적어도 대부분의 배수

if __name__ == '__main__':
    A = list(map(int, input().split()))
    result = min(A)
    while True:
        count = 0
        for num in A:
            if result % num == 0:
                count += 1
        if count >= 3:
            break
        result += 1
    print(result)

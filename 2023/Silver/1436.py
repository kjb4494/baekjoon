# https://www.acmicpc.net/problem/1436
# 영화감독 숌

if __name__ == '__main__':
    N = int(input())
    result = 666
    count = 0
    while True:
        if '666' in str(result):
            count += 1
        if count == N:
            print(result)
            break
        result += 1

# https://www.acmicpc.net/problem/1568
# 새

if __name__ == '__main__':
    N = int(input())
    current_num = 1
    result = 0
    while N > 0:
        if current_num > N:
            current_num = 1
        N -= current_num
        current_num += 1
        result += 1
    print(result)

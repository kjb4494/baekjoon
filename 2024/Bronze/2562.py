# https://www.acmicpc.net/problem/2562
# 최댓값

if __name__ == '__main__':
    A = [int(input()) for _ in range(9)]
    index = 0
    value = 0
    for i, num in enumerate(A):
        if value < num:
            value = num
            index = i + 1
    print(value)
    print(index)

# https://www.acmicpc.net/problem/1292
# 쉽게 푸는 문제

if __name__ == '__main__':
    NUM_TABLE = []
    current_num = 1
    while len(NUM_TABLE) < 1000:
        for i in range(current_num):
            NUM_TABLE.append(current_num)
        current_num += 1

    A, B = list(map(int, input().split()))
    print(sum(NUM_TABLE[A-1:B]))

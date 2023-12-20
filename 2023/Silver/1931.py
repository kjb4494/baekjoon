# https://www.acmicpc.net/problem/1931
# 회의실 배정

if __name__ == '__main__':
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    A.sort(key=lambda x: (x[1], x[0]))
    count = 0
    current_time = 0
    for a in A:
        if current_time <= a[0]:
            count += 1
            current_time = a[1]
    print(count)

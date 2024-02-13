# https://www.acmicpc.net/problem/1173
# 운동


if __name__ == '__main__':
    N, m, M, T, R = list(map(int, input().split()))

    if m + T > M:
        print(-1)
        exit()

    ex_time = 0
    total_time = 0
    pulse = m
    while ex_time < N:
        if pulse + T <= M:
            ex_time += 1
            pulse += T
        else:
            pulse -= R
            if pulse < m:
                pulse = m
        total_time += 1
    print(total_time)

# https://www.acmicpc.net/problem/1333
# 부재중 전화


if __name__ == '__main__':
    N, L, D = list(map(int, input().split()))
    time_table = [False] * N * (L + 5)
    for i in range(N):
        for j in range(5):
            time_table[(L * (i + 1)) + (i * 5) + j] = True
    current_d = D
    while True:
        if len(time_table) <= current_d:
            print(current_d)
            break

        if time_table[current_d]:
            print(current_d)
            break

        current_d += D

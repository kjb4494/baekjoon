
if __name__ == '__main__':
    N, M = list(map(int, input().split()))
    A = [input() for _ in range(N)]

    result = 0
    for i in range(N):
        for j in range(M):
            # 가로 나무 판자 체크: 현재 위치가 '-'이고, 왼쪽이 '-'가 아니거나 없는 경우
            if A[i][j] == '-' and (j == 0 or A[i][j-1] != '-'):
                result += 1
            # 세로 나무 판자 체크: 현재 위치가 '|'이고, 위쪽이 '|'가 아니거나 없는 경우
            if A[i][j] == '|' and (i == 0 or A[i-1][j] != '|'):
                result += 1

    print(result)

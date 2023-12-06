# https://www.acmicpc.net/problem/1236
# 성 지키기

def solve(n, m, castle):
    row_has_guard = [False] * N
    col_has_guard = [False] * M

    # 각 행과 열에 경비원이 있는지 확인
    for i in range(N):
        for j in range(M):
            if castle[i][j] == 'X':
                row_has_guard[i] = True
                col_has_guard[j] = True

    # 경비원이 없는 행과 열의 수 계산
    rows_needed = row_has_guard.count(False)
    cols_needed = col_has_guard.count(False)

    # 더 많은 경비원이 필요한 곳을 선택
    return max(rows_needed, cols_needed)


if __name__ == '__main__':
    N, M = map(int, input().split())
    CASTLE = [[c for c in input()] for _ in range(N)]
    print(solve(N, M, CASTLE))

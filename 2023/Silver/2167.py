# https://www.acmicpc.net/problem/2167
# 2차원 배열의 합

# 누적 합 배열 계산
def calculate_prefix_sum():
    result = [[0] * (M + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            result[i][j] = A[i - 1][j - 1] + result[i - 1][j] + result[i][j - 1] - result[i - 1][j - 1]
    return result


def solve(i, j, x, y):
    return PREFIX_SUM[x][y] - PREFIX_SUM[i - 1][y] - PREFIX_SUM[x][j - 1] + PREFIX_SUM[i - 1][j - 1]


if __name__ == '__main__':
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    PREFIX_SUM = calculate_prefix_sum()

    K = int(input())
    B = [list(map(int, input().split())) for _ in range(K)]
    for [i, j, x, y] in B:
        print(solve(i, j, x, y))

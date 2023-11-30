# https://www.acmicpc.net/problem/2740
# 행렬 곱셈

def solve(matrix1, matrix2):
    # 첫 번째 행렬의 행의 수와 열의 수
    rows_matrix1 = len(matrix1)
    cols_matrix1 = len(matrix1[0])
    cols_matrix2 = len(matrix2[0])

    # 결과 행렬 초기화
    result = [[0 for _ in range(cols_matrix2)] for _ in range(rows_matrix1)]

    # 행렬 곱셈 수행
    for i in range(rows_matrix1):
        for j in range(cols_matrix2):
            for k in range(cols_matrix1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result


if __name__ == '__main__':
    N, M = map(int, input().split())
    A = [[int(x) for x in list(input().split())] for _ in range(N)]
    M, K = map(int, input().split())
    B = [[int(x) for x in list(input().split())] for _ in range(M)]

    C = solve(A, B)

    for row in C:
        print(" ".join(map(str, row)))

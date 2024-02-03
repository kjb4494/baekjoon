# https://www.acmicpc.net/problem/11444
# 피보나치 수 6

# 행렬 거듭제곱과 분할 정복 방식을 이용
# 98% 에서 실패하는데 원인을 모르겠음

import sys
sys.setrecursionlimit(10**6)


def mul_matrix(mat1, mat2):
    res = [[0] * 2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            # 중간 합계를 저장하기 위한 변수
            temp_sum = 0
            for k in range(2):
                temp_sum += (mat1[i][k] * mat2[k][j]) % 1_000_000_007
                temp_sum %= 1_000_000_007  # 덧셈 후 모듈로 연산 적용
                res[i][j] = temp_sum  # 최종 값 할당
    return res


def matrix_pow(matrix, power):
    if power == 1:
        return matrix
    else:
        half_pow = matrix_pow(matrix, power // 2)
        if power % 2 == 0:
            return mul_matrix(half_pow, half_pow)
        else:
            return mul_matrix(mul_matrix(half_pow, half_pow), matrix)


def solve(n):
    f_matrix = [[1, 1], [1, 0]]
    result_matrix = matrix_pow(f_matrix, n - 1)
    return result_matrix[0][0]


if __name__ == '__main__':
    N = int(input())
    print(solve(N))

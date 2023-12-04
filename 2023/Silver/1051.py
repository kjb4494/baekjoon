# https://www.acmicpc.net/problem/1051
# 숫자 정사각형

def solve():
    square_max_size = min(N, M)
    result = 1

    if square_max_size == 1:
        return result

    for square_size in range(1, square_max_size + 1):
        for i in range(N - square_size):
            for j in range(M - square_size):
                if A[i][j] == A[i+square_size][j] == A[i][j+square_size] == A[i+square_size][j+square_size]:
                    result = square_size + 1
                    break
    return result * result


# 조기 중단 개선
# 큰 정사각형부터 탐색
def solve_better():
    square_max_size = min(N, M)
    result = 1

    for square_size in range(square_max_size, 0, -1):
        found = False
        for i in range(N - square_size + 1):
            for j in range(M - square_size + 1):
                if A[i][j] == A[i+square_size-1][j] == A[i][j+square_size-1] == A[i+square_size-1][j+square_size-1]:
                    result = square_size
                    found = True
                    break
            if found:
                break
        if found:
            break

    return result * result


if __name__ == '__main__':
    N, M = map(int, input().split())
    A = [[int(number) for number in input()] for _ in range(N)]
    print(solve_better())

# https://www.acmicpc.net/problem/9663
# N-Queen

def is_safe(row, col):
    for i in range(row):
        if (BOARD[i] == col or
                BOARD[i] - i == col - row or
                BOARD[i] + i == col + row):
            return False
    return True


def n_queens(row):
    if row == N:
        return 1
    count = 0
    for col in range(N):
        if is_safe(row, col):
            BOARD[row] = col
            count += n_queens(row + 1)
            BOARD[row] = -1
    return count


def solve():
    return n_queens(0)


if __name__ == '__main__':
    N = int(input())
    BOARD = [-1] * N
    print(solve())

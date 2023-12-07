# https://www.acmicpc.net/problem/2578
# 빙고

def is_bingo(board):
    n = len(board)
    bingo_count = 0  # 빙고 카운터

    # 가로 빙고 확인
    for row in board:
        if all(x == 0 for x in row):
            bingo_count += 1
            if bingo_count >= 3:  # 빙고 카운트가 3 이상이면 바로 True 반환
                return True

    # 세로 빙고 확인
    for col in range(n):
        if all(board[row][col] == 0 for row in range(n)):
            bingo_count += 1
            if bingo_count >= 3:
                return True

    # 대각선 빙고 확인 (왼쪽 위 -> 오른쪽 아래)
    if all(board[i][i] == 0 for i in range(n)):
        bingo_count += 1
        if bingo_count >= 3:
            return True

    # 대각선 빙고 확인 (오른쪽 위 -> 왼쪽 아래)
    if all(board[i][n - 1 - i] == 0 for i in range(n)):
        bingo_count += 1
        if bingo_count >= 3:
            return True

    return False


def solve():
    for count, num in enumerate(NUM_LIST):
        for i in range(5):
            for j in range(5):
                if BINGO_BOARD[i][j] == num:
                    BINGO_BOARD[i][j] = 0
                    if is_bingo(BINGO_BOARD):
                        return count + 1


if __name__ == '__main__':
    BINGO_BOARD = [list(map(int, input().split())) for _ in range(5)]
    NUM_LIST = []
    for _ in range(5):
        NUM_LIST.extend(map(int, input().split()))
    print(solve())

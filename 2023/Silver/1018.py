# https://www.acmicpc.net/problem/1018

def solve(board):
    min_repaint = float('inf')  # 최소 다시 칠해야 하는 정사각형 개수를 무한대로 초기화

    for i in range(len(board) - 7):
        for j in range(len(board[0]) - 7):
            repaint1 = 0  # 맨 왼쪽 위 칸이 흰색인 경우에서 다시 칠해야 하는 정사각형 개수
            repaint2 = 0  # 맨 왼쪽 위 칸이 검은색인 경우에서 다시 칠해야 하는 정사각형 개수

            for x in range(i, i + 8):
                for y in range(j, j + 8):
                    # (x, y) 좌표의 색을 확인하여 다시 칠해야 하는 경우를 계산
                    if (x + y) % 2 == 0:  # (x+y)가 짝수이면 흰색이어야 함
                        if board[x][y] != 'W':
                            repaint1 += 1
                        if board[x][y] != 'B':
                            repaint2 += 1
                    else:  # (x+y)가 홀수이면 검은색이어야 함
                        if board[x][y] != 'B':
                            repaint1 += 1
                        if board[x][y] != 'W':
                            repaint2 += 1

            min_repaint = min(min_repaint, repaint1, repaint2)

    return min_repaint


if __name__ == '__main__':
    N, M = map(int, input().split())
    board = [list(input()) for _ in range(N)]
    print(solve(board))

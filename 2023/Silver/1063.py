# https://www.acmicpc.net/problem/1063
# 킹

def chess_coord_to_index(coord):
    row = 8 - int(coord[1])
    col = ord(coord[0].upper()) - ord('A')
    return row, col


def move(current_loc, command: str):
    x, y = current_loc
    if 'R' in command:
        y += 1
    if 'L' in command:
        y -= 1
    if 'B' in command:
        x += 1
    if 'T' in command:
        x -= 1

    if 0 <= x < 8 and 0 <= y < 8:
        return x, y
    else:
        return current_loc


def solve():
    king_loc, stone_loc = KING_LOC, STONE_LOC
    for command in COMMAND_LIST:
        next_king_loc = move(king_loc, command)
        next_stone_loc = stone_loc
        # 킹과 돌이 같을 때
        if next_king_loc == stone_loc:
            next_stone_loc = move(stone_loc, command)
            # 돌의 다음 위치가 막혔을 때
            if next_stone_loc == stone_loc:
                next_king_loc = king_loc
                next_stone_loc = stone_loc
        king_loc = next_king_loc
        stone_loc = next_stone_loc
    return CHESS_BOARD[king_loc[0]][king_loc[1]], CHESS_BOARD[stone_loc[0]][stone_loc[1]]


if __name__ == '__main__':
    CHESS_BOARD = [[f"{chr(65 + col)}{8 - row}" for col in range(8)] for row in range(8)]
    tmp_input = input().split()
    KING_LOC, STONE_LOC, N = chess_coord_to_index(tmp_input[0]), chess_coord_to_index(tmp_input[1]), int(tmp_input[2])
    COMMAND_LIST = [input() for _ in range(N)]
    RESULT_KING_LOC, RESULT_STONE_LOC = solve()
    print(RESULT_KING_LOC)
    print(RESULT_STONE_LOC)

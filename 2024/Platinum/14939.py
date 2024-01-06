# https://www.acmicpc.net/problem/14939
# 불 끄기

from itertools import product


def switch_lights(grid, row, col):
    directions = [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)]
    for dr, dc in directions:
        nr, nc = row + dr, col + dc
        if 0 <= nr < 10 and 0 <= nc < 10:
            grid[nr][nc] = not grid[nr][nc]


def all_lights_off(grid):
    return all(not light for row in grid for light in row)


def solve():
    # 모든 전구를 끄기 위해 최소한으로 눌러야 하는 스위치의 개수
    min_switches = float('inf')

    # 첫 번째 행에 대해 가능한 모든 스위치 조작을 시도
    for switches in product([True, False], repeat=10):
        copy_grid = [row[:] for row in GRID]
        # 해당 사이클에서 전구를 끈 횟수
        count = 0

        for col, switch in enumerate(switches):
            if switch:
                switch_lights(copy_grid, 0, col)
                count += 1

        # 각 조합에 대해, 첫 번째 행의 조작을 바탕으로 나머지 행에서 필요한 스위치 조작을 결정
        for row in range(1, 10):
            for col in range(10):
                if copy_grid[row - 1][col]:
                    switch_lights(copy_grid, row, col)
                    count += 1

        # 마지막 행까지 모든 전구를 끌 수 있는지 확인
        if all_lights_off(copy_grid):
            min_switches = min(min_switches, count)

    return min_switches if min_switches != float('inf') else -1


if __name__ == '__main__':
    A = [input() for _ in range(10)]
    GRID = [[light == 'O' for light in row] for row in A]
    print(solve())

# https://www.acmicpc.net/problem/14502

"""
1. 입력으로 주어진 연구소 지도를 읽어옵니다.
2. 가능한 모든 벽을 세우는 경우의 수를 생성합니다. 이를 위해 중첩된 반복문이나 조합(combinations)을 사용할 수 있습니다.
3. 각 경우마다 벽을 세운 후, 바이러스의 확산을 시뮬레이션합니다. 이를 위해 너비 우선 탐색(BFS)이나 깊이 우선 탐색(DFS)을 사용하여 바이러스가 퍼지는 과정을 구현합니다.
4. 각 경우에 대해 안전 영역의 크기를 계산하고, 최댓값을 갱신합니다.
5. 모든 경우에 대한 안전 영역 크기 중에서 최댓값을 출력합니다.
"""

from itertools import combinations
from collections import deque


def spread_virus(lab, walls):
    # 복사본 생성
    new_lab = [row[:] for row in lab]

    # 벽 세우기
    for wall in walls:
        x, y = wall
        new_lab[x][y] = 1

    # 바이러스 퍼뜨리기 (BFS)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    for i in range(len(new_lab)):
        for j in range(len(new_lab[0])):
            if new_lab[i][j] == 2:
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < len(new_lab) and 0 <= ny < len(new_lab[0]) and new_lab[nx][ny] == 0:
                new_lab[nx][ny] = 2
                queue.append((nx, ny))

    # 안전 영역 크기 계산
    safe_area = sum(row.count(0) for row in new_lab)

    return safe_area


def max_safe_area(lab):
    n = len(lab)
    m = len(lab[0])
    empty_cells = [(i, j) for i in range(n) for j in range(m) if lab[i][j] == 0]
    wall_combinations = combinations(empty_cells, 3)
    max_area = 0

    for walls in wall_combinations:
        safe_area = spread_virus(lab, walls)
        max_area = max(max_area, safe_area)

    return max_area


if __name__ == "__main__":
    n, m = map(int, input().split())
    lab = [list(map(int, input().split())) for _ in range(n)]
    result = max_safe_area(lab)
    print(result)

# https://www.acmicpc.net/contest/problem/1206/14
# N번 - 크냑과 3D 프린터

def solve(n, heights):
    # 기본 겉넓이 계산 (각 막대의 앞면과 뒷면)
    total_surface_area = 2 * n  # 각 막대의 상단과 하단 면

    # 각 막대의 높이를 더하여 앞면과 뒷면을 계산
    total_surface_area += sum(heights) * 2

    # 이웃하는 막대 사이의 높이 차이에 따른 옆면 면적을 계산
    for i in range(1, n):
        total_surface_area += abs(heights[i] - heights[i - 1])

    # 첫 번째 및 마지막 막대의 옆면 추가
    total_surface_area += heights[0] + heights[-1]

    return total_surface_area


if __name__ == '__main__':
    N = int(input())
    HEIGHTS = list(map(int, input().split()))
    print(solve(N, HEIGHTS))

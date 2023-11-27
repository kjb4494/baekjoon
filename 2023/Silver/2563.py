# https://www.acmicpc.net/problem/2563

if __name__ == '__main__':
    # 도화지 초기화
    canvas = [[0] * 100 for _ in range(100)]

    # 색종이 수 입력
    num_papers = int(input())

    # 색종이를 도화지에 붙이면서 겹치는 부분 표시
    for _ in range(num_papers):
        x, y = map(int, input().split())
        for i in range(x, x + 10):
            for j in range(y, y + 10):
                canvas[i][j] = 1

    # 표시된 검은 영역의 넓이 계산
    black_area = sum(row.count(1) for row in canvas)

    print(black_area)

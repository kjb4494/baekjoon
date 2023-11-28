# https://www.acmicpc.net/problem/2669
# 직사각형 네개의 합집합의 면적 구하기

if __name__ == '__main__':
    canvas = [[0] * 100 for _ in range(100)]
    for i in range(4):
        x1, y1, x2, y2 = map(int, input().split())
        for xi in range(x1, x2):
            for yi in range(y1, y2):
                canvas[xi][yi] = 1
    print(sum(row.count(1) for row in canvas))

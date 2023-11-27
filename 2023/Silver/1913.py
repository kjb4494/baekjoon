# https://www.acmicpc.net/problem/1913

def snail_array(N, target):
    array = [[0] * N for _ in range(N)]
    x, y = N // 2, N // 2
    array[x][y] = 1

    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]  # 좌, 하, 우, 상
    num, direction, steps = 2, 0, 1

    while num <= N**2:
        for _ in range(2):
            for _ in range(steps):
                if num > N**2:
                    break
                x, y = x + dx[direction], y + dy[direction]
                array[x][y] = num
                num += 1
            direction = (direction + 1) % 4
        steps += 1

    target_x, target_y = [(ix, iy) for ix, row in enumerate(array) for iy, val in enumerate(row) if val == target][0]

    for row in array:
        print(' '.join(map(str, row)))
    print(target_x + 1, target_y + 1)


if __name__ == '__main__':
    N = int(input())
    target = int(input())
    snail_array(N, target)

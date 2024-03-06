# https://www.acmicpc.net/problem/1297
# TV 크기


if __name__ == '__main__':
    D, H, W = list(map(int, input().split()))

    x = H / W
    rh = (D ** 2 / (x ** 2 + 1)) ** 0.5
    rw = x * rh

    print(int(rw), int(rh))

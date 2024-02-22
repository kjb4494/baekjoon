# https://www.acmicpc.net/problem/1357
# 뒤집힌 덧셈

def rev(num):
    return int(str(num)[::-1])


if __name__ == '__main__':
    X, Y = list(map(int, input().split()))
    print(rev(rev(X) + rev(Y)))

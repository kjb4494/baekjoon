# https://www.acmicpc.net/problem/1439
# 뒤집기

def solve(s):
    flips = 0
    prev_char = s[0]

    for char in s:
        if char != prev_char:
            flips += 1
            prev_char = char

    return (flips + 1) // 2


if __name__ == '__main__':
    print(solve(input()))

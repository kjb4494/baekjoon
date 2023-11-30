# https://www.acmicpc.net/problem/1652
# 누울 자리를 찾아라

def solve(room):
    result = [0, 0]
    room_size = len(room)
    for i in range(room_size):
        count = 0
        for j in range(room_size):
            if room[i][j] == 'X':
                if count >= 2:
                    result[0] += 1
                count = 0
            else:
                count += 1
        if count >= 2:
            result[0] += 1

    for j in range(room_size):
        count = 0
        for i in range(room_size):
            if room[i][j] == 'X':
                if count >= 2:
                    result[1] += 1
                count = 0
            else:
                count += 1
        if count >= 2:
            result[1] += 1

    return " ".join(map(str, result))


if __name__ == '__main__':
    N = int(input())
    print(solve([list(input()) for _ in range(N)]))

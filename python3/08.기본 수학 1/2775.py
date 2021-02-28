if __name__ == '__main__':
    rooms = [[1] * 14 for _ in range(15)]
    for a in range(15):
        for b in range(14):
            if a == 0:
                rooms[a][b] = b + 1
                continue
            if b == 0:
                continue
            rooms[a][b] = rooms[a-1][b] + rooms[a][b-1]

    output = []

    T = int(input())
    for _ in range(T):
        k = int(input())
        n = int(input())
        output.append(str(rooms[k][n-1]))

    print('\n'.join(output))

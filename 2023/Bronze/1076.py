
if __name__ == '__main__':
    INFO_MAP = {
        'black': 0,
        'brown': 1,
        'red': 2,
        'orange': 3,
        'yellow': 4,
        'green': 5,
        'blue': 6,
        'violet': 7,
        'grey': 8,
        'white': 9
    }

    I_1 = str(INFO_MAP.get(input()))
    I_2 = str(INFO_MAP.get(input()))
    I_3 = '0' * INFO_MAP.get(input())

    print(int(I_1 + I_2 + I_3))

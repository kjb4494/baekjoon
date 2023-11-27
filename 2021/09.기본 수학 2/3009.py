from collections import Counter


if __name__ == '__main__':
    ixs = []
    iys = []
    for _ in range(3):
        x, y = map(int, input().split())
        ixs.append(x)
        iys.append(y)
    ixs = Counter(ixs)
    iys = Counter(iys)
    print(min(ixs, key=ixs.get), min(iys, key=iys.get))

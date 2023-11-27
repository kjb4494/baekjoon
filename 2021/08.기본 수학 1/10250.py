# 101, 201, 301, ..., H01,
# 102, 202, 302, ..., H02,
# ...
# 1W, 2W, 3W, ..., HW

def get_room(h, n):
    if n % h != 0:
        x = str(n // h + 1).zfill(2)
        y = str(n % h)
    else:
        x = str(n // h).zfill(2)
        y = str(h)
    return y + x


if __name__ == '__main__':
    test_case_count = int(input())
    result = []
    for _ in range(test_case_count):
        H, W, N = map(int, input().split())
        result.append(get_room(H, N))
    print('\n'.join(result))

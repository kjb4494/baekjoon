def is_hansu(n):
    str_n = str(n)
    n_len = len(str_n)
    if n_len < 3:
        return True
    difference = set()
    for i in range(1, n_len):
        difference.add(int(str_n[i]) - int(str_n[i-1]))
    return len(difference) == 1


if __name__ == '__main__':
    N = int(input())
    result = 0
    for X in range(1, N+1):
        if is_hansu(X):
            result += 1
    print(result)

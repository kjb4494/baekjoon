def factorial(n):
    if not isinstance(n, int):
        raise TypeError
    if n < 0:
        raise ValueError
    if n == 0:
        return 1
    return factorial(n-1) * n


if __name__ == '__main__':
    print(factorial(int(input())))

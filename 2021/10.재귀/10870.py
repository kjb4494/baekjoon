def fibonacci(n):
    if not isinstance(n, int):
        raise TypeError
    if not (0 <= n <= 20):
        raise ValueError
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n >= 2:
        return fibonacci(n-2) + fibonacci(n-1)


if __name__ == '__main__':
    print(fibonacci(int(input())))

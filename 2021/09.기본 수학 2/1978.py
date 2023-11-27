def get_prime_table(n):
    sieve = [False, False] + [True] * (n - 1)
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i]:
            for j in range(i + i, n + 1, i):
                sieve[j] = False
    return sieve


if __name__ == '__main__':
    T = int(input())
    inputs = list(map(int, input().split()[:T]))
    prime_table = get_prime_table(max(inputs))
    count = 0
    for num in inputs:
        if prime_table[num]:
            count += 1
    print(count)

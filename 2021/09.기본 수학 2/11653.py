def get_prime_table(n):
    sieve = [False, False] + [True] * (n - 1)
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i]:
            for j in range(i + i, n + 1, i):
                sieve[j] = False
    return sieve


def get_factorization(num):
    prime_table = get_prime_table(num)
    for prime in [n for n, is_prime in enumerate(prime_table) if is_prime]:
        while num % prime == 0:
            num /= prime
            print(prime)


if __name__ == '__main__':
    get_factorization(int(input()))

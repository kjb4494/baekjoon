def get_prime_table(n):
    sieve = [False, False] + [True] * (n - 1)
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i]:
            for j in range(i + i, n + 1, i):
                sieve[j] = False
    return sieve


if __name__ == '__main__':
    M, N = map(int, input().split())
    prime_table = get_prime_table(N)
    primes = [num for num in range(M, N + 1) if prime_table[num]]
    for prime in primes:
        print(prime)

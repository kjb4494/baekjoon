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
    inputs = [int(input()) for _ in range(T)]
    prime_table = get_prime_table(max(inputs))
    for i_num in inputs:
        for x in range(i_num//2, 0, -1):
            if prime_table[x] and prime_table[i_num-x]:
                print(x, i_num-x)
                break

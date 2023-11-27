def get_prime_table(n):
    sieve = [False, False] + [True] * (n - 1)
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i]:
            for j in range(i + i, n + 1, i):
                sieve[j] = False
    return sieve


if __name__ == '__main__':
    inputs = []
    while True:
        num = int(input())
        if num == 0:
            break
        inputs.append(num)
    prime_table = get_prime_table(max(inputs) * 2)
    for i_num in inputs:
        count = 0
        for num in range(i_num + 1, i_num * 2 + 1):
            if prime_table[num]:
                count += 1
        print(count)

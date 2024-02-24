# https://www.acmicpc.net/problem/2153
# 소수 단어

def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def letter_to_number_ascii(letter):
    if letter.islower():
        return ord(letter) - ord('a') + 1
    else:
        return ord(letter) - ord('A') + 27


if __name__ == '__main__':
    S = input()
    word_sum = 0
    for c in S:
        word_sum += letter_to_number_ascii(c)
    print("It is a prime word." if is_prime(word_sum) else "It is not a prime word.")

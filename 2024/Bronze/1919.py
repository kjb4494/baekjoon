# https://www.acmicpc.net/problem/1919
# 애너그램 만들기

from collections import Counter


if __name__ == '__main__':
    A = input()
    B = input()

    A_counter = Counter(A)
    B_counter = Counter(B)

    a = sum((A_counter - B_counter).values())
    b = sum((B_counter - A_counter).values())
    print(a + b)

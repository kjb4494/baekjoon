# https://www.acmicpc.net/contest/problem/1206/15
# O번 - A+B - 10 (제2편)

import random


def ask_judge(query):
    print(query, flush=True)
    return int(input())


def find_value(name):
    possible_values = set(range(1, 10001))
    while len(possible_values) > 1:
        guess = random.choice(list(possible_values))
        response = ask_judge(f"? {name} {guess}")
        if response == 1:
            return guess
        possible_values.remove(guess)
    return possible_values.pop()


A = find_value("A")
B = find_value("B")


print(f"! {A + B}")

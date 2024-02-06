# https://www.acmicpc.net/problem/10816
# 숫자 카드 2

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    M = int(input())
    B = list(map(int, input().split()))

    A_map = {}
    for card_num in A:
        if not A_map.get(card_num):
            A_map[card_num] = 1
        else:
            A_map[card_num] += 1

    results = []
    for b in B:
        results.append(A_map.get(b) if A_map.get(b) is not None else 0)

    print(" ".join(map(str, results)))

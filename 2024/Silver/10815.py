# https://www.acmicpc.net/problem/10815
# 숫자 카드

if __name__ == '__main__':
    N = int(input())
    A = {key: 1 for key in list(map(int, input().split()))}
    M = int(input())
    B = list(map(int, input().split()))

    results = []
    for num in B:
        results.append(str(A.get(num)) if A.get(num) else "0")
    print(" ".join(results))

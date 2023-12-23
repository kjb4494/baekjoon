import sys
from itertools import permutations

input = sys.stdin.readline


def calculate_taste(N, K, sweetness, saltiness, noticeability, order):
    total_taste = 0
    prev_notice = 0

    for i in range(1, N):
        current_notice = noticeability[order[i - 1]] * noticeability[order[i]]

        if current_notice > K:
            return -1

        total_taste += sweetness[order[i - 1]] * saltiness[order[i]]

    return total_taste


def solve():
    N, K = map(int, input().split())
    sweetness = list(map(int, input().split()))
    saltiness = list(map(int, input().split()))
    noticeability = list(map(int, input().split()))

    # 가능한 모든 순서에 대해 총 감칠맛을 계산
    max_taste = -1
    for order in permutations(range(N), N):
        taste = calculate_taste(N, K, sweetness, saltiness, noticeability, order)
        max_taste = max(max_taste, taste)

    # 결과 출력
    print(max_taste)


# 입력 처리
if __name__ == '__main__':
    solve()

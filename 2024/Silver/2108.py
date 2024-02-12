# https://www.acmicpc.net/problem/2108
# 통계학

import sys
from collections import Counter


input = sys.stdin.readline


if __name__ == '__main__':
    N = int(input())
    A = [int(input()) for _ in range(N)]
    A.sort()

    # 산술 평균
    print(round(sum(A) / N))

    # 중앙값
    print(A[len(A) // 2])

    # 최빈값
    counter = Counter(A)
    most_common_elements = counter.most_common()
    max_count = most_common_elements[0][1]
    mode_candidates = [element for element, count in most_common_elements if count == max_count]
    print(sorted(mode_candidates)[1] if len(mode_candidates) > 1 else mode_candidates[0])

    # 범위
    print(A[-1] - A[0])

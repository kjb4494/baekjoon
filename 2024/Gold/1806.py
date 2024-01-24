# https://www.acmicpc.net/problem/1806
# 부분합


""" 시간복잡도가 너무 높음
if __name__ == '__main__':
    N, S = list(map(int, input().split()))
    A = list(map(int, input().split()))

    # 누적합 리스트
    sum_list = [A[0]]
    for i in range(1, len(A)):
        sum_list.append(sum_list[i-1] + A[i])

    # 연속된 수 최소 길이
    result = float('inf')
    for i in range(1, len(sum_list)):
        if sum_list[i] < S:
            continue

        for j in range(0, i):
            if sum_list[i] - sum_list[j] >= S:
                result = min(result, i - j)

    print(result)
"""

# 슬라이딩 윈도우를 이용한 두 포인터 전략
import sys

input = sys.stdin.readline

if __name__ == '__main__':
    N, S = list(map(int, input().split()))
    A = list(map(int, input().split()))

    left, right = 0, 0
    min_length = float('inf')
    current_sum = 0

    while right < len(A):
        current_sum += A[right]
        right += 1

        while current_sum >= S:
            min_length = min(min_length, right - left)
            current_sum -= A[left]
            left += 1

    print(min_length if min_length != float('inf') else 0)

# https://www.acmicpc.net/contest/problem/1206/7
# G번 - Enigmatic Device 2023

import sys


# 시간 초과로 실패함
def solve():
    # 0부터 2022까지의 숫자에 대한 제곱 % 2023의 결과를 미리 계산
    square_mod = [i ** 2 % 2023 for i in range(2023)]

    # 결과를 저장할 리스트
    results = []

    # 각 연산을 순차적으로 수행
    for op in operations:
        k, l, r = op

        if k == 1:  # 1번 연산: 구간 업데이트
            for i in range(l - 1, r):
                a[i] = square_mod[a[i]]

        elif k == 2:  # 2번 연산: 구간 합 계산
            results.append(sum(a[l - 1:r]))

    for result in results:
        print(result)


# 역시 시간 초과 남 ㅠㅠ
def solve_optimized():
    # 0부터 2022까지의 숫자에 대한 제곱 % 2023의 결과를 미리 계산
    square_mod = [i ** 2 % 2023 for i in range(2023)]

    # 업데이트가 필요한 구간을 표시하는 플래그 배열 초기화
    update_needed = [False] * n

    # 결과를 저장할 문자열
    results_str = ""

    # 각 연산을 순차적으로 수행
    for op in operations:
        k, l, r = op

        if k == 1:  # 1번 연산: 구간 업데이트 표시
            for i in range(l - 1, r):
                update_needed[i] = True

        elif k == 2:  # 2번 연산: 구간 합 계산
            # 필요한 경우에만 업데이트 수행
            sum_result = 0
            for i in range(l - 1, r):
                if update_needed[i]:
                    a[i] = square_mod[a[i]]
                    update_needed[i] = False
                sum_result += a[i]

            # 구간 합 계산
            results_str += f"{sum_result}\n"

    return results_str[:-1]


if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    a = list(map(int, sys.stdin.readline().strip().split()))
    m = int(sys.stdin.readline().strip())
    operations = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(m)]

    print(solve_optimized())

# https://www.acmicpc.net/contest/problem/1215/1
# A번 - 진주로 가자! (Easy)

import sys

input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    TRANSPORT = [input().split() for _ in range(N)]

    # 진주로 가는 교통편 요금 찾기
    jinju_fare = next(int(fare) for dest, fare in TRANSPORT if dest == 'jinju')

    # 진주로 가는 교통편보다 비싼 교통편의 개수 세기
    more_expensive = sum(int(fare) > jinju_fare for dest, fare in TRANSPORT)

    # 결과 출력
    print(jinju_fare)
    print(more_expensive)

# https://www.acmicpc.net/contest/problem/1215/2
# B번 - 진주로 가자! (Hard)
# ! 메모리 초과로 틀림... 어디가 문제인지 모르겠음; 10의 15승 문자열을 받는 곳이 문제인거같기도...

import sys

input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    jinju_fare = None
    more_expensive_count = 0
    temp_fares = []

    for _ in range(N):
        destination, fare = input().split()
        fare = int(fare)

        if destination == 'jinju':
            jinju_fare = fare
            more_expensive_count += sum(temp_fare > jinju_fare for temp_fare in temp_fares)
        else:
            if jinju_fare is not None:
                if fare > jinju_fare:
                    more_expensive_count += 1
            else:
                temp_fares.append(fare)

    print(jinju_fare)
    print(more_expensive_count)

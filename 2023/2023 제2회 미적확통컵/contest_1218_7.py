# https://www.acmicpc.net/contest/problem/1218/7
# PA번 - 자동차 주차

from math import factorial


# Function to calculate the number of ways to park the cars
def calculate_parking_ways(n, a, b, c):
    return factorial(n) // (factorial(a) * factorial(b) * factorial(c))


# Calculate the number of ways for the example input
if __name__ == '__main__':
    N, A, B, C = list(map(int, input().split()))
    print(calculate_parking_ways(N, A, B, C))

# https://www.acmicpc.net/problem/11399
# ATM


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    result = A[0]
    current_sum = A[0]
    for i in range(1, N):
        current_sum += A[i]
        result += current_sum
    print(result)

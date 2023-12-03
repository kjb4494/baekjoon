# https://www.acmicpc.net/problem/1024
# 수열의 합

# 연속된 정수들의 합 공식 = (첫번째 수 + 마지막 수) X 수의 개수 / 2
# 문제에서 첫번째 수를 x라고할 때 n과 l이 주어지므로, 마지막 수는 x + l - 1이므로 x를 간소화할 수 있다.
def solve(n, l):
    for length in range(l, 101):
        # x: 첫번째 수
        x = (n - (length * (length - 1) // 2)) / length
        if x.is_integer() and x >= 0:
            return " ".join([str(int(x) + i) for i in range(length)])
    return -1


if __name__ == '__main__':
    N, L = map(int, input().split())
    print(solve(N, L))

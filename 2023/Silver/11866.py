# https://www.acmicpc.net/problem/11866
# 요세푸스 문제 0

def solve(n, k):
    circle_list = [i + 1 for i in range(n)]
    result = []
    current_index = 0
    while len(circle_list) > 0:
        current_index = (current_index + k - 1) % len(circle_list)
        result.append(circle_list.pop(current_index))
    return "<" + ", ".join(map(str, result)) + ">"


if __name__ == '__main__':
    N, K = map(int, input().split())
    print(solve(N, K))

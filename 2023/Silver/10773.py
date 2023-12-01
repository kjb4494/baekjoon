# https://www.acmicpc.net/problem/10773
# 제로

def solve(K, numbers):
    result_list = []
    for num in numbers:
        if num == 0:
            result_list.pop()
        else:
            result_list.append(num)
    return sum(result_list)


if __name__ == '__main__':
    K = int(input())
    numbers = [int(input()) for _ in range(K)]
    print(solve(K, numbers))

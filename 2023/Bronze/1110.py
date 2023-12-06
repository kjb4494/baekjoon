# https://www.acmicpc.net/problem/1110
# 더하기 사이클

def solve(n):
    # ab -> a + b = c -> new_num = (b * 10) + (c % 10)
    result = 0
    tmp_num = n
    while True:
        a = tmp_num // 10
        b = tmp_num % 10
        c = a + b
        tmp_num = b * 10 + c % 10
        result += 1
        if tmp_num == n:
            break
    return result


if __name__ == '__main__':
    N = int(input())
    print(solve(N))

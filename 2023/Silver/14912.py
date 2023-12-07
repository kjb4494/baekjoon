# https://www.acmicpc.net/problem/14912
# 숫자 빈도수

if __name__ == '__main__':
    n, d = map(int, input().split())
    str_d = str(d)
    result = 0
    for num in range(1, n+1):
        str_num = str(num)
        result += str_num.count(str_d)
    print(result)

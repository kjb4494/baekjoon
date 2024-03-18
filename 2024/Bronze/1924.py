# https://www.acmicpc.net/problem/1924
# 2007년

if __name__ == '__main__':
    month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    x, y = list(map(int, input().split()))
    days = 0
    for i in range(x - 1):
        days += month[i]
    days += y
    print(day[days % 7])

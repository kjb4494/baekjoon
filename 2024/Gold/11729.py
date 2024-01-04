# https://www.acmicpc.net/problem/11729
# 하노이 탑 이동 순서

# n개의 원반을 aux를 경유하여 start 기둥에서 end 기둥으로 이동
def solve(n, start, end, aux):
    if n == 1:
        RESULTS.append("{} {}".format(start, end))
        return

    solve(n-1, start, aux, end)
    RESULTS.append("{} {}".format(start, end))
    solve(n-1, aux, end, start)


if __name__ == '__main__':
    N = int(input())
    RESULTS = []
    solve(N, 1, 3, 2)
    print(len(RESULTS))
    for result in RESULTS:
        print(result)

# https://www.acmicpc.net/problem/1427
# 소트인사이드

if __name__ == '__main__':
    N = list(input())
    N.sort(reverse=True)
    print("".join(N))

# https://www.acmicpc.net/problem/9461
# 파도반 수열


if __name__ == '__main__':
    P = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
    T = int(input())
    results = []
    for _ in range(T):
        n = int(input())
        if n <= len(P):
            results.append(P[n-1])
        else:
            for i in range(len(P) - 1, n - 1):
                P.append(P[i-1] + P[i-2])
            results.append(P[n-1])
    for result in results:
        print(result)

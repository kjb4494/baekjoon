# https://www.acmicpc.net/problem/10798
# 세로읽기


if __name__ == '__main__':
    A = [list(input()) for _ in range(5)]
    result = ""
    for i in range(15):
        for j in range(5):
            try:
                result += A[j][i]
            except:
                pass
    print(result)

# https://www.acmicpc.net/problem/2577
# 숫자의 개수

if __name__ == '__main__':
    doc = {str(i): 0 for i in range(10)}
    A = int(input())
    B = int(input())
    C = int(input())
    num_str = str(A * B * C)
    for c in num_str:
        doc[c] += 1
    for i in range(10):
        print(doc[str(i)])

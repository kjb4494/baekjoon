# https://www.acmicpc.net/problem/10820
# 문자열 분석

if __name__ == '__main__':
    while True:
        try:
            S = list(input())
            result = [0, 0, 0, 0]
            for c in S:
                if c.islower():
                    result[0] += 1
                elif c.isupper():
                    result[1] += 1
                elif c.isnumeric():
                    result[2] += 1
                elif c == ' ':
                    result[3] += 1
            print(' '.join(map(str, result)))
        except EOFError:
            break

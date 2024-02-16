# https://www.acmicpc.net/problem/1251
# 단어 나누기


if __name__ == '__main__':
    S = input()
    result = set()

    for i in range(1, len(S) - 1):
        for j in range(i + 1, len(S)):
            first = S[:i][::-1]
            second = S[i:j][::-1]
            third = S[j:][::-1]
            result.add(first + second + third)

    print(min(result))

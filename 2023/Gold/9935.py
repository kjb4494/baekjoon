# https://www.acmicpc.net/problem/9935
# 문자열 폭발

if __name__ == '__main__':
    S = input()
    C = input()
    stack = []
    c_len = len(C)
    for c in S:
        stack.append(c)
        if len(stack) >= c_len and "".join(stack[-c_len:]) == C:
            del stack[-c_len:]

    result = ''.join(stack)
    print(result if result else "FRULA")

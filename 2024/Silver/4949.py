# https://www.acmicpc.net/problem/4949
# 균형잡힌 세상


def solve():
    results = []
    while True:
        s = input()
        if s == '.':
            return results
        stack = []
        for c in s:
            if c == '[' or c == '(':
                stack.append(c)
            elif c == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    stack.append(']')
                    break
            elif c == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(')')
                    break
        results.append("no" if stack else "yes")


if __name__ == '__main__':
    for result in solve():
        print(result)

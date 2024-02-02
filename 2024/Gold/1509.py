# 팰린드롬 분할

def solve():
    n = len(S)
    # is_palindrome[i][j]는 S[i:j+1]이 팰린드롬인지 여부를 저장
    is_palindrome = [[False] * n for _ in range(n)]
    # min_cuts[i]는 S[:i+1]을 팰린드롬으로 분할할 때 필요한 최소 분할 횟수를 저장
    min_cuts = [0] * n

    for i in range(n):
        min_cut = i
        for j in range(i + 1):
            if S[i] == S[j] and (i - j < 2 or is_palindrome[j + 1][i - 1]):
                is_palindrome[j][i] = True
                min_cut = 0 if j == 0 else min(min_cut, min_cuts[j - 1] + 1)
        min_cuts[i] = min_cut

    return min_cuts[-1] + 1


if __name__ == '__main__':
    S = input()
    print(solve())

# https://www.acmicpc.net/problem/17413
# 단어 뒤집기 2

def solve(s):
    current_word_start_index = 0
    is_in_tag = False
    for i in range(len(s)):
        if s[i] == '<':
            s = s[:current_word_start_index] + s[current_word_start_index:i][::-1] + s[i:]
            current_word_start_index = i + 1
            is_in_tag = True
        elif s[i] == '>':
            current_word_start_index = i + 1
            is_in_tag = False
        elif s[i] == ' ' and not is_in_tag:
            s = s[:current_word_start_index] + s[current_word_start_index:i][::-1] + s[i:]
            current_word_start_index = i + 1
        elif i == len(s) - 1 and not is_in_tag:
            s = s[:current_word_start_index] + s[current_word_start_index:][::-1]
    return s


# 정규 표현식을 사용해 코드량 자체는 줄었지만 정규식 자체가 읽기 어렵고 수행시간과 메모리 사용량이 기존거보다 떨어짐
def solve_better(s):
    import re

    # 태그, 단어, 공백을 찾는 정규 표현식
    tokens = re.findall(r'<[^>]+>|[^<\s]+|\s+', s)

    # 태그가 아닌 단어만 뒤집고, 나머지는 그대로 유지
    return ''.join(token[::-1] if token.strip() and not token.startswith('<') else token for token in tokens)


if __name__ == '__main__':
    S = input()
    print(solve_better(S))

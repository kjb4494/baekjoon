# https://www.acmicpc.net/problem/1371
# 가장 많은 글자

import sys
from collections import Counter

if __name__ == '__main__':
    # 입력 문자열 처리
    S = ""
    while True:
        line = sys.stdin.readline()
        if line == '':
            break
        S += line

    # 띄어쓰기, 줄바꿈 제거
    text = S.replace(" ", "").replace("\n", "")

    # 알파뱃 카운팅
    letter_counts = Counter(text)

    # 가장 높은 빈도수 찾기
    max_freq = max(letter_counts.values())

    # 해당 빈도수를 가진 모든 글자 찾기
    most_common_letters = [letter for letter, freq in letter_counts.items() if freq == max_freq]

    # 결과를 알파벳 순으로 정렬
    most_common_letters.sort()

    # 결과 출력
    print(''.join(most_common_letters))

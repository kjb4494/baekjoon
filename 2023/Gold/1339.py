# 단어 수학
# https://www.acmicpc.net/problem/1339

if __name__ == '__main__':
    N = int(input())
    WORDS = [[c for c in input()] for _ in range(N)]
    alphabet_weights = {}

    # 각 알파뱃의 가중치 계산
    for word in WORDS:
        weight = 1
        for char in reversed(word):
            if char in alphabet_weights:
                alphabet_weights[char] += weight
            else:
                alphabet_weights[char] = weight
            weight *= 10

    # 가중치에 따라 숫자 할당
    sorted_weights = sorted(alphabet_weights.items(), key=lambda x: x[1], reverse=True)
    num = 9
    number_map = {}
    for char, _ in sorted_weights:
        number_map[char] = num
        num -= 1

    # 최종 합 계산
    result = 0
    for word in WORDS:
        number = ''.join(str(number_map[char]) for char in word)
        result += int(number)
    print(result)

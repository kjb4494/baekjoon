# https://www.acmicpc.net/problem/1546
# 평균


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))

    max_score = max(A)
    score_sum = 0
    for score in A:
        score_sum = score_sum + score / max_score * 100
    print(score_sum / len(A))

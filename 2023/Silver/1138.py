# https://www.acmicpc.net/problem/1138
# 한 줄로 서기

if __name__ == '__main__':
    N = int(input())
    heights = list(map(int, input().split()))
    result = [0] * N

    for i in range(N):
        count = heights[i]  # i번째 사람의 왼쪽에 있는 더 큰 사람 수
        for j in range(N):
            if result[j] == 0 and count == 0:
                result[j] = i + 1  # 순서를 결정하고 다음 사람으로 넘어감
                break
            elif result[j] == 0:
                count -= 1

    print(" ".join(map(str, result)))

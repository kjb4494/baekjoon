# https://www.acmicpc.net/problem/1783
# 병든 나이트

def solve():
    # 체스판의 세로 길이가 1인 경우, 나이트는 이동할 수 없음
    if N == 1:
        return 1

    # 체스판의 세로 길이가 2인 경우,
    # '2칸 위로, 1칸 오른쪽', '2칸 아래로, 1칸 오른쪽'만 사용 가능
    if N == 2:
        return min(4, (M + 1) // 2)

    # 체스판의 가로 길이가 7보다 작은 경우,
    # 모든 이동 방법을 사용하기에는 공간이 충분하지 않으므로, 최대 4칸까지만 이동 가능
    if M < 7:
        return min(4, M)

    # 그 외의 경우, 나이트는 체스판을 자유롭게 이동 가능
    return M - 2


if __name__ == '__main__':
    N, M = map(int, input().split())
    print(solve())

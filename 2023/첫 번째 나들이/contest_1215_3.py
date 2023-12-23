import sys

input = sys.stdin.readline


def select_miniatures(miniatures, quality_first=True):
    if quality_first:
        # 품질 우선, 가격 차선으로 정렬
        miniatures.sort(key=lambda x: (-x[0], x[1]))
    else:
        # 가격 우선, 품질 차선으로 정렬
        miniatures.sort(key=lambda x: (x[1], -x[0]))

    # 첫 번째와 두 번째 아이템 선택
    return miniatures[0], miniatures[1]


if __name__ == '__main__':
    # 입력 처리
    N = int(input())
    miniatures = [tuple(map(int, input().split())) for _ in range(N)]

    # 첫 번째 방법으로 선택
    first_choice = select_miniatures(miniatures.copy(), quality_first=True)
    print(*first_choice[0], *first_choice[1])

    # 두 번째 방법으로 선택
    second_choice = select_miniatures(miniatures, quality_first=False)
    print(*second_choice[0], *second_choice[1])

# https://www.acmicpc.net/problem/2161

def solve(n):
    num_list = [i for i in range(n)]
    discard_this_turn = True
    result = []

    while len(num_list) != 0:
        if discard_this_turn:
            result.append(num_list.pop(0) + 1)
            discard_this_turn = not discard_this_turn
        else:
            num_list.append(num_list.pop(0))
            discard_this_turn = not discard_this_turn

    return " ".join(map(str, result))


# 이 코드는 큐를 이용하여 숫자를 처리하며, 큐가 빌 때까지 숫자를 빼내고 다시 큐에 넣는 방식으로 작동합니다.
# 이 방법은 불필요한 리스트 슬라이싱과 pop(0) 연산을 피할 수 있어 좀 더 효율적입니다.
# --> 큐를 사용하면 더 빠를 줄 알았는데 오히려 큐 연산 때문인지 약 30%의 성능 저하가 발생함. 더 좋은 코드는 아닌듯함.
def solve_better(n):
    from collections import deque

    queue = deque(i for i in range(1, n + 1))
    result = []

    while queue:
        result.append(queue.popleft())
        if queue:
            queue.append(queue.popleft())

    return " ".join(map(str, result))


if __name__ == '__main__':
    print(solve_better(int(input())))

# https://www.acmicpc.net/problem/10866
# 덱

from collections import deque


class SolveDeque:
    def __init__(self):
        self.deque_list = deque()

    def push_front(self, val):
        self.deque_list.appendleft(val)

    def push_back(self, val):
        self.deque_list.append(val)

    def pop_front(self):
        if len(self.deque_list) == 0:
            print(-1)
        else:
            print(self.deque_list.popleft())

    def pop_back(self):
        if len(self.deque_list) == 0:
            print(-1)
        else:
            print(self.deque_list.pop())

    def size(self):
        print(len(self.deque_list))

    def empty(self):
        if len(self.deque_list) == 0:
            print(1)
        else:
            print(0)

    def front(self):
        if len(self.deque_list) == 0:
            print(-1)
        else:
            print(self.deque_list[0])

    def back(self):
        if len(self.deque_list) == 0:
            print(-1)
        else:
            print(self.deque_list[-1])

    def command(self, cmd: str):
        split_cmd = cmd.split()

        if len(split_cmd) == 2:
            if split_cmd[0] == "push_back":
                self.push_back(split_cmd[1])
            else:
                self.push_front(split_cmd[1])
        elif split_cmd[0] == "pop_front":
            self.pop_front()
        elif split_cmd[0] == "pop_back":
            self.pop_back()
        elif split_cmd[0] == "size":
            self.size()
        elif split_cmd[0] == "empty":
            self.empty()
        elif split_cmd[0] == "front":
            self.front()
        else:
            self.back()

    def exec_commands(self, cmd_list):
        for cmd in cmd_list:
            self.command(cmd)


if __name__ == '__main__':
    N = int(input())
    solve_stack = SolveDeque()
    solve_stack.exec_commands([input() for _ in range(N)])

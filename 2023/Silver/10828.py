# https://www.acmicpc.net/problem/10828
# 스택

class SolveStack:
    def __init__(self):
        self.stack_list = []

    def push(self, val):
        self.stack_list.append(val)

    def top(self):
        if len(self.stack_list) == 0:
            print(-1)
        else:
            print(self.stack_list[-1])

    def size(self):
        print(len(self.stack_list))

    def empty(self):
        if len(self.stack_list) == 0:
            print(1)
        else:
            print(0)

    def pop(self):
        if len(self.stack_list) == 0:
            print(-1)
        else:
            print(self.stack_list.pop())

    def command(self, cmd: str):
        split_cmd = cmd.split()

        # push
        if len(split_cmd) == 2:
            self.push(split_cmd[1])
        elif split_cmd[0] == "pop":
            self.pop()
        elif split_cmd[0] == "size":
            self.size()
        elif split_cmd[0] == "empty":
            self.empty()
        else:
            self.top()

    def exec_commands(self, cmd_list):
        for cmd in cmd_list:
            self.command(cmd)


if __name__ == '__main__':
    N = int(input())
    solve_stack = SolveStack()
    solve_stack.exec_commands([input() for _ in range(N)])

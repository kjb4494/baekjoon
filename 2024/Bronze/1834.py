# https://www.acmicpc.net/problem/1834
# 나머지와 몫이 같은 수

def solve():
    result = 0
    for i in range(1, N):
        num = i * N + i # i(N+1)
        result += num
        # => (1+2+3+...+(N-1))(N+1) = (N(N-1)//2)(N+1)
    return result


def solve_better():
    return ((N*(N-1))//2)*(N+1)


if __name__ == '__main__':
    N = int(input())
    print(solve_better())

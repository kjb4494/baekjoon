# https://www.acmicpc.net/problem/2491
# 수열

def solve(a):
    larger_counts = [1]
    smaller_counts = [1]
    for i in range(1, len(a)):
        if a[i] >= a[i-1]:
            larger_counts[-1] += 1
        else:
            larger_counts.append(1)

        if a[i] <= a[i-1]:
            smaller_counts[-1] += 1
        else:
            smaller_counts.append(1)

    return max(max(larger_counts), max(smaller_counts))


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    print(solve(A))

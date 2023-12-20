import heapq

if __name__ == '__main__':
    N = int(input())
    A = [int(input()) for _ in range(N)]
    heapq.heapify(A)
    result = 0
    while len(A) > 1:
        first = heapq.heappop(A)
        second = heapq.heappop(A)

        result += first + second

        heapq.heappush(A, first + second)
    print(result)

if __name__ == '__main__':
    N, M = map(int, input().split())
    cards = list(map(int, input().split()))[:N]
    results = []
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            for k in range(j + 1, N):
                cards_sum = cards[i] + cards[j] + cards[k]
                if cards_sum == M:
                    print(cards_sum)
                    exit()
                if cards_sum > M:
                    continue
                results.append(cards_sum)
    print(max(results))

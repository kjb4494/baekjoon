import sys

input = sys.stdin.readline

if __name__ == '__main__':
    T = int(input())

    results = []
    for _ in range(T):
        s = input().strip()
        # (, ) 개수가 다름
        if s.count(")") != s.count("("):
            results.append(False)
            continue

        # 조건부 카운팅
        count = 0
        for c in s:
            if c == ")" and count > 0:
                count -= 1
            else:
                count += 1
        results.append(count == 0)

    # 출력
    for result in results:
        print("YES" if result else "NO")

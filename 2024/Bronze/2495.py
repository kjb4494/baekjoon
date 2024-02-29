# https://www.acmicpc.net/problem/2495
# 연속구간

if __name__ == '__main__':
    results = []
    for _ in range(3):
        input_num = input()
        max_count = 1
        current_num_count = 1

        for i in range(1, len(input_num)):
            if input_num[i-1] == input_num[i]:
                current_num_count += 1
                max_count = max(max_count, current_num_count)
            else:
                current_num_count = 1

        results.append(max_count)

    for result in results:
        print(result)

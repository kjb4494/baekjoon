# https://www.acmicpc.net/problem/1032
# 명령 프롬프트

def solve(file_name_list):
    result = list(file_name_list[0])
    for i in range(1, len(file_name_list)):
        for j in range(len(file_name_list[i])):
            if file_name_list[i][j] != result[j]:
                result[j] = '?'
    return "".join(result)


if __name__ == '__main__':
    N = int(input())
    FILE_NAME_LIST = [input() for _ in range(N)]
    print(solve(FILE_NAME_LIST))

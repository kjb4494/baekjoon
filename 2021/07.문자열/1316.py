def is_group_word(word):
    current_c = ''
    appeared_c_list = []
    for c in word:
        if current_c != c:
            if c in appeared_c_list:
                return False
            current_c = c
            appeared_c_list.append(c)
    return True


if __name__ == '__main__':
    repeat = int(input())
    words = []
    for _ in range(repeat):
        words.append(input())
    result = 0
    for wd in words:
        if is_group_word(wd):
            result += 1
    print(result)

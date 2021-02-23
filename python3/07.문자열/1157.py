if __name__ == '__main__':
    c_map = {}
    most_count = 0
    for c in input().lower():
        try:
            c_map[c] += 1
        except KeyError:
            c_map.update({c: 1})
        if most_count < c_map[c]:
            most_count = c_map[c]
    result = []
    for key, value in c_map.items():
        if most_count == value:
            result.append(key)
    if len(result) == 1:
        print(result[0].upper())
    else:
        print('?')

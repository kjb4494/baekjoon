def is_right_triangle(a, b, c):
    ab = [a, b, c]
    c = max(a, b, c)
    ab.remove(c)
    return ab[0]**2 + ab[1]**2 == c**2


if __name__ == '__main__':
    output = []
    while True:
        x, y, z = map(int, input().split())
        if x == 0 and y == 0 and z == 0:
            break
        if is_right_triangle(x, y, z):
            output.append('right')
        else:
            output.append('wrong')
    print('\n'.join(output))


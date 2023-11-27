# d^2 = (x2 - x1)^2 + (y2 - y1)^2
# 0개: r1 + r2 < d or r1 - r2 > d
# 1개: r1 + r2 = d or r1 - r2 = d
# 2개: r1 - r2 < d < r1 + r2

def get_distance(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5


def get_count_of_intersection_point(r1, r2, d):
    if r1 == r2 and d == 0:
        return -1
    if r1 + r2 < d or abs(r1 - r2) > d:
        return 0
    if r1 + r2 == d or abs(r1 - r2) == d:
        return 1
    return 2


if __name__ == '__main__':
    output = []
    T = int(input())
    for _ in range(T):
        i_x1, i_y1, i_r1, i_x2, i_y2, i_r2 = map(int, input().split())
        distance = get_distance(x1=i_x1, y1=i_y1, x2=i_x2, y2=i_y2)
        output.append(str(get_count_of_intersection_point(r1=i_r1, r2=i_r2, d=distance)))
    print('\n'.join(output))

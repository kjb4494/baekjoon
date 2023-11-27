import math


def get_area_from_euclidean(r):
    return r * r * math.pi


def get_area_from_non_euclidean(r):
    return r * r * 2.0


if __name__ == '__main__':
    R = int(input())
    print(get_area_from_euclidean(R))
    print(get_area_from_non_euclidean(R))

def get_break_even_point(fixed_cost, production_cost, product_price):
    if production_cost >= product_price:
        return -1

    # fixed_cost + production_cost * n < product_price * n
    # fixed_cost / (product_price - production_cost) < n

    return fixed_cost // (product_price - production_cost) + 1


if __name__ == '__main__':
    A, B, C = map(int, input().split())
    print(get_break_even_point(A, B, C))

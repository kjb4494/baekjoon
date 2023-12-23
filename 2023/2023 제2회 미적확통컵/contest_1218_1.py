# https://www.acmicpc.net/contest/problem/1218/1
# CA번 - 하루 피부과

# Function f(x) - g(x)
def integrand(x, a, b, c, d, e):
    return a * x ** 2 + (b - d) * x + (c - e)


# Function to integrate and calculate the laser intensity
def calculate_laser_intensity(x1, x2, a, b, c, d, e):
    # Integrate the function from x1 to x2
    integral_x1 = (a / 3) * x1 ** 3 + (b - d) / 2 * x1 ** 2 + (c - e) * x1
    integral_x2 = (a / 3) * x2 ** 3 + (b - d) / 2 * x2 ** 2 + (c - e) * x2
    return integral_x2 - integral_x1


if __name__ == '__main__':
    x1, x2 = list(map(int, input().split()))
    a, b, c, d, e = list(map(int, input().split()))
    print(int(calculate_laser_intensity(x1, x2, a, b, c, d, e)))

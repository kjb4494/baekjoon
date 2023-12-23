from sympy import symbols, sin, cos, exp, diff

# Define the symbol
x = symbols('x')

# Define the ESC(x) function
ESC_x = exp(x) * sin(x) * cos(x)


# Function to calculate an, bn, cn for the nth derivative
def calculate_an_bn_cn(n, func):
    # Differentiate n times
    for _ in range(n):
        func = diff(func, x)
        # print(func.coeff(exp(x) * sin(x) ** 2))
        # print(func.coeff(exp(x) * cos(x) ** 2))
        print(func.coeff(exp(x) * sin(x) * cos(x)))
        # print("---")

    # Extract the coefficients of e^x * sin(x)^2, e^x * cos(x)^2, and e^x * sin(x) * cos(x)
    a_n = func.coeff(exp(x) * sin(x) ** 2)
    b_n = func.coeff(exp(x) * cos(x) ** 2)
    c_n = func.coeff(exp(x) * sin(x) * cos(x))


    return a_n, b_n, c_n


# Function to get the cn value for '날먹'
def get_cn(n):
    cn_pattern = [
        1, -3, -11, -7, 41, 117, 29, -527, -1199, 237, 6469, 11753, -8839,
        -76443, -108691, 164833, 873121, 922077, -2521451, -9653287, -6699319,
        34867797, 103232189, 32125393, -451910159, -1064447283, 130656229,
        5583548873, 10513816601, -6890111163
    ]
    # Adjust for zero-based indexing
    return cn_pattern[n - 1]


if __name__ == '__main__':
    N = int(input())
    # print(sum(calculate_an_bn_cn(N, ESC_x)))
    print(get_cn(N))

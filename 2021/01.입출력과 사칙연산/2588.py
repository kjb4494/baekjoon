if __name__ == '__main__':
    num_1 = int(input())
    num_2 = int(input())
    for i in str(num_2)[::-1]:
        print(num_1 * int(i))
    print(num_1 * num_2)

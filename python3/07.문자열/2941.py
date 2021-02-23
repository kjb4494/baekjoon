cas = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

if __name__ == '__main__':
    input_str = input()
    for ca in cas:
        input_str = input_str.replace(ca, '1')
    print(len(input_str))

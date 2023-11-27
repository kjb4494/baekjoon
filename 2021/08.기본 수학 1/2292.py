# 1, 7, 19, 37, 61
# 6*0+1, 6*1+1, 6*3+1, 6*6+1, 6*10+1, ...
# 6*0+1, 6*(0+1)+1, 6*(0+1+2)+1, 6*(0+1+2+3)+1, 6*(0+1+2+3+4)+1, ...

if __name__ == '__main__':
    num = int(input())

    room = 1
    variables = 0

    while True:
        if num <= 6 * variables + 1:
            print(room)
            break
        variables += room
        room += 1

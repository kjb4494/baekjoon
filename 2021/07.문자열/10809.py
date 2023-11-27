import string

if __name__ == '__main__':
    alphabet = dict.fromkeys(string.ascii_lowercase, -1)
    for i, c in enumerate(input()):
        if alphabet[c] == -1:
            alphabet[c] = i
    print(' '.join([str(value) for key, value in alphabet.items()]))

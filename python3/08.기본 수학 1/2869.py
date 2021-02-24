# V >= An - B(n-1)
# (V - B) / (A - B) >=  n

if __name__ == '__main__':
    A, B, V = map(int, input().split())
    print((V - B) // (A - B) + 1 if (V - B) % (A - B) != 0 else (V - B) // (A - B))

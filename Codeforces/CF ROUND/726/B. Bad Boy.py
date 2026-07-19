def sol():
    n, m, i, j = map(int, input().split())

    if i != 1 and j != 1 and i != n and j != m:
        print("1 1", n, m)
    else:
        print("1", m , n , "1")


tc = int(input())
while tc:
    tc-=1
    sol()
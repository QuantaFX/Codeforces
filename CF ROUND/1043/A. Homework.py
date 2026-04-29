def sol():
    n = int(input())
    a = input()
    m = int(input())
    b = input()
    c = input()

    for i in range(m):
        if c[i] == 'D':
            a += b[i]
        else:
            a = b[i] + a
    print(a)

tc = int(input())
while tc:
    tc-=1
    sol()
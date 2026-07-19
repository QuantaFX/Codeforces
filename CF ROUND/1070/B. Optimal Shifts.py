def sol():
    n = int(input())
    a = list(input())

    m = 0
    for i in range(n):
        r = (i+1)%n
        if a[i] == '1' and a[r] == '0':
            c = 0
            while a[r] == '0':
                c += 1
                i += 1
                r = (r+1)%n
            m = max(m, c)
    print(m)

tc = int(input())
while tc:
    sol()
    tc-=1
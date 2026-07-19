def sol():
    a, b = map(int, input().split())

    if b%2 == 0:
        a *= (b//2)
        b = 2
    else:
        a *= b
        b = 1

    if (a+b) % 2 == 0:
        print(int(a+b))
    else:
        print(-1)


tc = int(input())
while tc:
    tc -= 1
    sol()
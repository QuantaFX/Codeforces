def sol():
    n = int(input())

    if n%2 ==0:
        print(n-3, 2, 1)
    else:
        n -= 1
        if n % 4 == 0:
            a = n // 2 -1
            b = n // 2 + 1
            print(a, b, 1)
        else:
            a = n // 2 - 2
            b = n // 2 + 2
            print(a, b, 1)
tc = int(input())
while tc:
    tc -= 1
    sol()
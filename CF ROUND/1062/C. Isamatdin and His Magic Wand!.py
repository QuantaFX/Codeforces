def sol():
    n = int(input())
    a = list(map(int, input().split()))

    odd = False
    even = False

    for i in range(n):
        if a[i] % 2 == 0:
            even = True
        else:
            odd = True

    if odd and even:
        s = sorted(a)
        print(*s)
    else:
        print(*a)

tc = int(input())
while tc:
    tc -=1
    sol()
def sol():
    n = int(input())

    s = int(n/7)
    if n % 7 != 0:
        s += 1
    print(s)

tc = int(input())
while tc > 0:
    tc -= 1
    sol()
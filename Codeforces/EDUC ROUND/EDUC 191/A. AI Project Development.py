import math

def sol():
    n, x, y, z = map(int, input().split())

    normal_rate = math.ceil(n/(x+y))

    i = 0
    while n > 0:
        i += 1
        n -= x
        if i > z:
            n -= 10*y
        if i > normal_rate:
            break

    if i > normal_rate:
        print(normal_rate)
    else:
        print(i)

tc = int(input())
while tc:
    tc -=1
    sol()

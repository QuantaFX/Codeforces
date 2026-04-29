def sol():
    y, x = map(int, input().split())

    maxi = max(y, x)
    square = maxi * maxi
    if maxi % 2 == 0:
        square -= maxi - y
        square -= x - 1
    else:
        square -= maxi - x
        square -= y - 1
    print(square)

tc = int(input())
while tc:
    sol()
    tc -= 1
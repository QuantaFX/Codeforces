def sol():
    x, y, r = map(int, input().split())

    print(x, y+r)

tc = int(input())
while tc:
    tc -= 1
    sol()
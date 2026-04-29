def sol():
    x, n = map(int, input().split())

    if n%2 == 0:
        print(0)
    else:
        print(x)

tc = int(input())
while tc:
    tc-=1
    sol()
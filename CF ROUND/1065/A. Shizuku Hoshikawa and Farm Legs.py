def sol():
    n = int(input())

    if n%2 == 1:
        print(0)
    else:
        print(n//4 + 1)

tc = int(input())
while tc:
    tc -= 1
    sol()
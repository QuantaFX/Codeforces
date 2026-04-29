def sol():
    k, x = map(int, input().split())

    for i in range(k):
        x *= 2

    print(x)
tc = int(input())
while tc:
    tc -= 1
    sol()
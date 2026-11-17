def sol():
    n = int(input())
    a = list(map(int, input().split()))

    for i in range(n-4):
        print(a[i], a[i+2], a[i+4])

tc = int(input())
while tc:
    tc -= 1
    sol()
def sol():
    n = int(input())
    a = [i for i in range(1,3*n+1)]

    l = 0
    r = 3*n-2

    for i in range(n):
        print(a[l], a[r], a[r+1], end=" ")
        l += 1
        r -= 2
    print()

tc = int(input())
while tc:
    sol()
    tc -= 1
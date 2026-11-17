def sol():
    n = int(input())
    a = list(map(int, input().split()))

    for i in range(n):
        if a[i] == 1:
            break
        if a[i] == -1:
            a[i] = 1
            break

    for i in range(n-1, -1, -1):
        if a[i] == 1:
            break
        if a[i] == -1:
            a[i] = 1
            break

    for i in range(n):
        if a[i] == -1:
            a[i] = 0

    print(*a)

tc = int(input())
while tc:
    tc -= 1
    sol()
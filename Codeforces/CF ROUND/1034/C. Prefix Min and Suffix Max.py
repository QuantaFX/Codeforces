def sol():
    n = int(input())
    a = list(map(int, input().split()))

    l = [0] * n
    mini = max(a)
    maxi = min(a)

    for i in range(n):
        mini = min(mini, a[i])
        if a[i] == mini:
            l[i] = 1

    for i in range(n-1, -1, -1):
        maxi = max(maxi, a[i])
        if a[i] == maxi:
            l[i] = 1

    for i in range(n):
        print(l[i], end="")
    print()

tc = int(input())
while tc:
    sol()
    tc -= 1
def sol():
    n = int(input())
    a = list(map(int, input().split()))

    for i in range(n):
        if a[i] == n-i:
            print(a[i], end=" ")
        else:
            x = a.index(n-i) + 1
            s = a[i:x]
            print(*s[::-1], *a[x:], end=" ")
            break
    print()

tc = int(input())
while tc:
    tc -= 1
    sol()
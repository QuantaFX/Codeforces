def sol():
    n, j, k = map(int, input().split())
    a = list(map(int, input().split()))

    if k == 1 and max(a) != a[j-1]:
        print("NO")
    else:
        print("YES")

tc = int(input())
while tc:
    sol()
    tc -= 1
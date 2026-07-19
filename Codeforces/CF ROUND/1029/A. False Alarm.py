def sol():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    start, end = 0, 0
    for i in range(n):
        if a[i] == 1:
            start = i
            break

    for i in range(n-1, -1, -1):
        if a[i] == 1:
            end = i
            break

    if end-start+1 > x:
        print("NO")
    else:
        print("YES")

tc = int(input())
while tc:
    tc -= 1
    sol()
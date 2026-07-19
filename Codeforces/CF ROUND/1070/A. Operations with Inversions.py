def sol():
    n = int(input())
    a = list(map(int, input().split()))

    m = a[0]
    ans = 0
    for i in range(n):
        m = max(a[i], m)
        if a[i] < m:
            ans += 1
    print(ans)

tc = int(input())
while tc:
    sol()
    tc -= 1
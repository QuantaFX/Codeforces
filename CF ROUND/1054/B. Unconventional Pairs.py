def sol():
    n = int(input())
    a = list(map(int, input().split()))
    a = sorted(a)

    ans = 0
    for i in range(0, n, 2):
        diff = a[i+1] - a[i]
        ans = max(ans, diff)

    print(ans)

tc = int(input())
while tc:
    tc -= 1
    sol()
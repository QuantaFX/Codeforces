def sol():
    n = int(input())
    s = list(map(int, input().split()))

    a = [0]*101
    for i in range(n):
        a[s[i]] += 1

    ans = 0
    for i in range(101):
        if a[i] >= i:
            ans += a[i] - i
        else:
            ans += a[i]

    print(ans)

tc = int(input())
while tc:
    tc -=1
    sol()
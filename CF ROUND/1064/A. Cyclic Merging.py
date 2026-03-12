def sol():
    n = int(input())
    s = list(map(int, input().split()))

    s.append(s[0])

    ans = 0
    for i in range(n):
        ans += max(s[i], s[i + 1])
    ans -= max(s)

    print(ans)

tc = int(input())
while tc:
    tc -=1
    sol()
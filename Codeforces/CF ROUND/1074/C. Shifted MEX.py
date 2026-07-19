def sol():
    n = int(input())
    a = list(map(int, input().split()))
    s = sorted(a)

    prev = s[0]
    ans, maxi = 1, 1
    for i in range(1, n):
        if s[i] <= prev+1:
            if s[i] == prev+1:
                ans += 1
                maxi = max(ans, maxi)
        else:
            ans = 1

        prev = s[i]

    print(maxi)

tc = int(input())
while tc:
    tc -= 1
    sol()
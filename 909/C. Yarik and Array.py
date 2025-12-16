def sol():
    n = int(input())
    s = list(map(int, input().split()))

    maxi = s[0]
    maxj = s[0]
    for i in range(1, n):
        if s[i] % 2 != s[i-1] % 2:
            if maxi < 0:
                maxi = s[i]
            else:
                maxi += s[i]
        else:
            maxi = s[i]
        if maxi > maxj:
            maxj = maxi
    print(maxj)

tc = int(input())
while tc:
    tc -= 1
    sol()
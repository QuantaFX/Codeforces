def sol():
    n, m = map(int, input().split())
    s = list(map(int, input().split()))

    maxi = max(s)
    for i in range(m):
        o, l, r = map(str, input().split())
        l = int(l)
        r = int(r)

        if l <= maxi <= r:
            if o == "+":
                maxi += 1
            else:
                maxi -= 1

        print(maxi, end=" ")
    print()

tc = int(input())
while tc:
    tc -=1
    sol()
def sol():
    n = int(input())
    s = list(map(int, input().split()))

    s.sort()

    f = True
    for i in range(n-1):
        if i % 2 == 1:
            if s[i] != s[i+1]:
                f = False
    if f:
        print("YES")
    else:
        print("NO")

tc = int(input())
while tc:
    tc -= 1
    sol()
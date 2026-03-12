def sol():
    s = list(map(int, input().split()))

    c = s[0]
    f = True
    for i in s:
        if i != c:
            f = False
    if f:
        print("YES")
    else:
        print("NO")
tc = int(input())
while tc:
    tc -=1
    sol()
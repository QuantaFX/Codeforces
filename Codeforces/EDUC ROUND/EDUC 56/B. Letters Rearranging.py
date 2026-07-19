def sol():
    s = input()

    s = sorted(s)
    c = s[0]
    f = True
    for i in s[1:]:
        if i != c:
            f = False
            break

    if f:
        print(-1)
    else:
        for i in s:
            print(i, end='')
        print()


tc = int(input())
while tc > 0:
    tc -= 1
    sol()
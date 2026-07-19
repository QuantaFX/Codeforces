def sol():
    x, y = map(int, input().split())
    a, b = map(int, input().split())

    y1 = max(x, y)
    x1 = min(x, y)
    s = (y1 - x1) * a

    if 2*a < b:
        s += x1 * 2 * a
        print(s)
    else:
        s += x1 * b
        print(s)


tc = int(input())
while tc:
    tc-=1
    sol()
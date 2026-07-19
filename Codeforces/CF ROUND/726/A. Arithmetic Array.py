def sol():
    n = int(input())
    s = map(int, input().split())

    c_s = sum(s)
    if c_s < n:
        print(1)
    elif c_s == n:
        print(0)
    else:
        print(c_s - n)

tc = int(input())
while tc:
    tc-=1
    sol()
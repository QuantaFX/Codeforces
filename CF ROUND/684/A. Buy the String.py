def sol():
    n, a, b, h = list(map(int, input().split()))
    s = input()

    z = s.count('0')
    o = s.count('1')

    if a==b:
        print(a*n)
    elif a<b:
        if b*o + a*z > a*n + h*o:
            print(a*n + h*o)
        else:
            print(b*o + a*z)
    elif a>b:
        if b*o + a*z > b*n + h*z:
            print(b*n + h*z)
        else:
            print(b*o + a*z)

tc = int(input())
while tc > 0:
    tc -= 1
    sol()
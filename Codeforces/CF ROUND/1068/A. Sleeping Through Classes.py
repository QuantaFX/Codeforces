def sol():
    n, k = map(int, input().split())
    s = list(input())

    c = 0
    out = 0

    for i in range(n):
        if s[i] == "1":
            c = k
        elif c == 0:
            out += 1
        elif c != 0:
            c -= 1

    print(out)

tc = int(input())
while tc > 0:
    tc -= 1
    sol()
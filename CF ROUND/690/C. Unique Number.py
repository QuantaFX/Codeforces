def sol():
    n = int(input())
    s = ""
    if n > 45:
        print(-1)
    else:
        for i in range(9, 0, -1):
            if n - i >= 0:
                s += str(i)
                n -= i
        print(s[::-1])

tc = int(input())
while tc:
    tc -= 1
    sol()
def sol():
    a, b = map(int, input().split())
    a, b = bin(a)[2:], bin(b)[2:]

    if b == a or len(b) > len(a):
        if b == a: print(0)
        else: print(-1)
        return

    if len(a) > len(b): print(2)
    else: print(1)

    b = "0" * (len(a) - len(b)) + b
    c = [0]*len(a)
    for i in range(1, len(a)):
        c[i] = 1 if a[i] != b[i] else 0
    print(int("".join(map(str, c)), 2), end=" ")

    if a[0] != b[0]: print(2**(len(a)-1))
    else: print()

tc = int(input())
while tc:
    tc -=1
    sol()
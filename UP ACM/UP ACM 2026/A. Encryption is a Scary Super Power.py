def sol():
    x, y = map(int, input().split())
    n = int(input())
    s = input()

    k = x+y
    if x == 0 and y == 0:
        k += 1
    k %= 26

    for i in range(n):
        p = ord(s[i]) + k
        if p > ord('z'):
            p -= 26
        print(chr(p), end="")
    print()

tc = int(input())
while tc:
    tc-=1
    sol()
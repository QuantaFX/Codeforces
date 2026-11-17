import math

def sol():
    n, x, y = map(int, input().split())
    p = list(map(int, input().split()))

    g = math.gcd(x, y)

    possible = True
    for i in range(n):
        if (i+1) % g !=  p[i] % g:
            possible = False
            break

    if possible:
        print("YES")
    else:
        print("NO")

tc = int(input())
while tc:
    tc -= 1
    sol()
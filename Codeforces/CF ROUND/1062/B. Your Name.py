def sol():
    n = int(input())
    a, b = map(str, input().split())
    a = sorted(a)
    b = sorted(b)
    if a == b:
        print("YES")
    else:
        print("NO")

tc = int(input())
while tc:
    tc -=1
    sol()
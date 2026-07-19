def sol():
    n = int(input())
    a = list(map(int, input().split()))

    if 67 in a:
        print("YES")
    else:
        print("NO")

tc = int(input())
while tc:
    tc -= 1
    sol()
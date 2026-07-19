def sol():
    x, y = map(int, input().split())

    if x % y == 0:
        print("YES")
    else:
        print("NO")

tc = int(input())
while tc:
    tc -=1
    sol()
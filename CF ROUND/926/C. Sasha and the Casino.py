def sol():
    k, x, a = map(int, input().split())

    lost = 0
    for i in range(x+1):
        lost += lost // (k-1) + 1
        if lost > a:
            print("NO")
            return
    print("YES")

tc = int(input())
while tc:
    tc -=1
    sol()
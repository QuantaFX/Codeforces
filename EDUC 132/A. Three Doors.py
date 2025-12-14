def sol():
    n = int(input())
    li = list(map(int, input().split()))

    if li[n-1] == 0:
        print("NO")
    elif li[li[n-1]-1] == 0:
        print("NO")
    else:
        print("YES")

tc = int(input())
while tc > 0:
    tc -= 1
    sol()
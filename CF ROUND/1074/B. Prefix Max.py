def sol():
    n = int(input())
    a = list(map(int, input().split()))

    maxi = max(a)
    print(maxi*n)

tc = int(input())
while tc:
    tc -= 1
    sol()
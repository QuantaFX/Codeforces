import math

def sol():
    n, k = map(int, input().split())
    l, r = n, n

    count = 0
    while r >= k:
        l = math.floor(n / 2**count)
        r = math.ceil(n / 2**count)
        if l <= k <= r:
            print(count)
            return
        count += 1
    print(-1)

tc = int(input())
while tc:
    tc -= 1
    sol()
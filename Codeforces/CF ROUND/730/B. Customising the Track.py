def sol():
    n = int(input())
    s = list(map(int, input().split()))

    sums = sum(s)
    r = sums % n
    print(r * (n - r))

tc = int(input())
while tc:
    tc -= 1
    sol()
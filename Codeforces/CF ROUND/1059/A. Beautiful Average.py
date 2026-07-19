def sol():
    n = int(input())
    a = list(map(int, input().split()))

    print(max(a))

tc = int(input())
while tc:
    tc -=1
    sol()
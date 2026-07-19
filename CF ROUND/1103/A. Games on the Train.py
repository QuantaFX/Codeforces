def sol():
    n = int(input())
    a = list(map(int, input().split()))

    maxi = max(a)
    mini = min(a)

    print(maxi - mini + 1)

tc = int(input())
while tc:
    sol()
    tc -= 1

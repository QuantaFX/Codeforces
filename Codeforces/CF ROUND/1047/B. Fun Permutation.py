def sol():
    n = int(input())
    p = list(map(int, input().split()))

    for i in range(n):
        print(n + 1 - p[i], end=" ")
    print()

tc = int(input())
while tc:
    tc -= 1
    sol()
def sol():
    n = int(input())
    s = list(map(int, input().split()))

    len, prev = 0, 0
    for i in range(n):
        if s[i] < prev:
            print(1)
            return
        prev = s[i]
    print(n)

tc = int(input())
while tc:
    tc -= 1
    sol()
def sol():
    n = int(input())
    s = list(map(int, input().split()))

    m = 1
    for i in range(0, n, 2):
        if s[i] > m:
            m = s[i]
    print(m)

tc = int(input())
while tc:
    tc -= 1
    sol()
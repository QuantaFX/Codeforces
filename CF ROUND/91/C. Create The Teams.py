def sol():
    n, m = map(int, input().split())
    s = list(map(int, input().split()))

    s.sort(reverse=True)

    c = 0
    t = 0
    for i in range(n):
        c += 1
        if s[i] * c >= m:
            t += 1
            c = 0

    print(t)

tc = int(input())
while tc:
    tc -=1
    sol()
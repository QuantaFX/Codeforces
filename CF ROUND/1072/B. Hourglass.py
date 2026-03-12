def sol():
    s, k, n = map(int, input().split())

    turns = n//k
    lapse = n%k
    if turns % 2 == 0:
        val = s
    else:
        val = min(s, k)

    if val > lapse:
        print(val - lapse)
    else:
        print(0)


tc = int(input())
while tc:
    sol()
    tc -= 1
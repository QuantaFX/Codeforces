def sol():
    a = list(map(int, input().split()))
    a.sort()

    SUM = 0
    for i in a:
        SUM -= i
    SUM += 2*(a[-1])

    print(SUM)

tc = int(input())
while tc:
    sol()
    tc -= 1
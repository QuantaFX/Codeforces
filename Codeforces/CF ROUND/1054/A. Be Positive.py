def sol():
    n = int(input())
    a = list(map(int, input().split()))

    neg = 0
    zero = 0

    for i in range(n):
        if a[i] < 0:
            neg += 1
        if a[i] == 0:
            zero += 1

    ans = 0
    if neg % 2 == 1:
        ans += 2
    ans += zero

    print(ans)

tc = int(input())
while tc:
    tc -=1
    sol()
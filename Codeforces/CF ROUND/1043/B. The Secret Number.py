def sol():
    n = int(input())

    ans = set()
    k = 1
    while True:
        div = 10**k + 1
        if div > n:
            break
        if n % div == 0:
            x = n // div
            ans.add(x)
        k+=1

    ans = sorted(ans)
    print(len(ans))
    if ans:
        print(*ans)

tc = int(input())
while tc:
    tc-=1
    sol()
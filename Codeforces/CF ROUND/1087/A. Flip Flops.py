def sol():
    n, c, k = map(int, input().split())
    a = list(map(int, input().split()))
    a = sorted(a)

    for i in a:
        if i <= c:
            added = min(k, c-i)
            c += i+added
            k -= added
        else:
            break

    print(c)
tc = int(input())
while tc:
    tc-=1
    sol()
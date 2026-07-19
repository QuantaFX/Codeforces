def sol():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    queries = []
    for i in range(q):
        l, r = map(int, input().split())
        queries.append((l,r))

    # MAXIMUM A
    for i in range(n):
        if a[i] < b[i]:
            a[i] = b[i]

    for i in range(n-2, -1, -1):
        if a[i+1] > a[i]:
            a[i] = a[i+1]

    # SUMMATION
    sum = 0
    a = [0] + a
    for i in range(n+1):
        sum += a[i]
        a[i] = sum

    for l, r in queries:
        print(a[r] - a[l-1], end=" ")
    print()

tc = int(input())
while tc:
    tc -= 1
    sol()
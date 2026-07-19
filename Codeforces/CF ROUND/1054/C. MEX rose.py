def sol():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    a.sort()
    c = a.count(k)

    i = len(set(x for x in a if x < k))

    print(max(k-i, c))


tc = int(input())
while tc:
    tc -= 1
    sol()
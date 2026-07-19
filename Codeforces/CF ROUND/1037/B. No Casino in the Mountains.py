def sol():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    ans, length = 0, 0
    peaked = False

    for i in a:
        if peaked:
            peaked = False
            length = 0
            continue

        if i == 0:
            length += 1
        else:
            length = 0

        if length == k:
            ans += 1
            peaked = True

    print(ans)

tc = int(input())
while tc:
    sol()
    tc -= 1
def sol():
    n = int(input())

    ans = [-1] * n
    for i in range(1, n, 2): ans[i] = 3
    if n%2 == 0: ans[-1] = 2

    print(*ans)

tc = int(input())
while tc:
    tc -= 1
    sol()
def sol():
    n = int(input())
    s = list(map(int, input().split()))

    s.sort()

    s[0] += 1

    ans = 1
    for i in s:
        ans *= i

    print(ans)

tc = int(input())
while tc:
    tc -=1
    sol()
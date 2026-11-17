def sol():
    a, b, c = map(int, input().split())

    if a == b or b == c or a == c:
        print(0)
        return

    else:
        ans = min(abs(a-b), abs(c-a), abs(b-c))
        print(ans)

tc = int(input())
while tc:
    tc -= 1
    sol()
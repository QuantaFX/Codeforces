def sol():
    n, s, x = map(int, input().split())
    a = list(map(int, input().split()))

    diff = s - sum(a)
    if diff % x == 0 and sum(a) <= s:
        print("YES")
    else:
        print("NO")

tc = int(input())
while tc:
    tc -= 1
    sol()
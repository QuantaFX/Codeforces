def sol():
    n = int(input())
    s = list(map(int, input().split()))

    loc = s.index(min(s))
    if loc == n-1:
        print(n-1)
    else:
        s2 = s[loc:]
        if s2 == sorted(s2):
            print(loc)
        else:
            print(-1)
tc = int(input())
while tc:
    tc -= 1
    sol()
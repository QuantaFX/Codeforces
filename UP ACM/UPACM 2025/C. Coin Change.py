def sol():
    n = int(input())

    ans = 0
    if n == 2:
        ans = 1
    else:
        ans = 6

    print("Case #", test-tc, ": ", ans, sep='')

tc = int(input())
test = tc
while tc:
    tc-=1
    sol()
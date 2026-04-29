def sol():
    n = int(input())
    s = list(map(int, input().split()))

    s.sort()

    sums = 0
    for i in range(n//2):
        sums += s[n-i-1] - s[i]

    print("Case #", test-tc, ": ", sums, sep='')


tc = int(input())
test = tc
while tc:
    tc-=1
    sol()
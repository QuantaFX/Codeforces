def sol():
    n, h = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    orig_h = h
    min_hp = h
    for i in range(n):
        h -= a[i]
        if h < min_hp:
            min_hp = h
        h += b[i]

    if h >= orig_h:
        print("Case #", test-tc, ": ", -1, sep='')
        return
    ans = 1
    max_dmg = orig_h - min_hp
    round_dmg = orig_h - h
    ans += (orig_h-max_dmg) // round_dmg
    if (orig_h-max_dmg) % round_dmg != 0:
        ans += 1
    print("Case #", test-tc, ": ", ans, sep='')

tc = int(input())
test = tc
while tc:
    tc-=1
    sol()
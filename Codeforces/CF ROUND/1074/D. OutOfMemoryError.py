def sol():
    n, m, h = map(int, input().split())
    a = list(map(int, input().split()))

    add = [0] * n
    changed = []
    for i in range(m):
        b, c = map(int, input().split())
        if add[b-1] + a[b-1] + c > h:
            for idx in changed:
                add[idx] = 0
            changed = []
        else:
            if add[b-1] == 0:
                changed.append(b-1)
            add[b-1] += c

    for i in range(n):
        a[i] += add[i]

    print(*a)

tc = int(input())
while tc:
    tc -= 1
    sol()
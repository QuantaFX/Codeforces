def sol():
    n, m = map(int, input().split())
    s = list(map(int, input().split()))

    hp = []
    for i in range(n):
        hp.append(((s[i]), i+1))
    hp.sort()
    max_hp = hp[-1][0]
    a = []

    k = 0
    for i in range(n-m):
        a_hp, a_add = hp[i]
        m_hp, m_add = hp[-1]

        a.append((a_add, m_add))
        max_hp -= m_hp
        k += 1

    print(len(a))
    for x, y in a:
        print(x, y)


tc = int(input())
while tc:
    tc -= 1
    sol()
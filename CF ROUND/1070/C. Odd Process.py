def sol():
    n = int(input())
    m = list(map(int, input().split()))

    e = []
    o = []
    for i in m:
        if i % 2 == 0:
            e.append(i)
        else:
            o.append(i)

    e = sorted(e, reverse=True)
    o = sorted(o, reverse=True)

    len_o = len(o)
    len_e = len(e)

    s = 0
    e_sum = [0]
    for i in range(len_e):
        s += e[i]
        e_sum.append(s)

    if len_o != 0:
        m_o = o[0]
    else:
        m_o = 0

    for i in range(1, n + 1):
        if len_o == 0:
            print(0, end=" ")
        else:
            odds = i - len_e
            if odds < 1:
                l = 1
            else:
                l = odds

            if len_o < i:
                u = len_o
            else:
                u = i

            if l > u:
                print(0, end=" ")
            else:
                if l % 2 != 0:
                    x = l
                else:
                    x = l + 1
                if x > u:
                    print(0, end=" ")
                else:
                    y = i - x
                    score = m_o + e_sum[y]
                    print(score, end=" ")
    print()

tc = int(input())
while tc > 0:
    tc -= 1
    sol()
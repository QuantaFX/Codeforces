def sol():
    n, m, h = map(int, input().split())

    r_ans = 0
    r_pen = 0
    pos = 1

    for i in range(n):
        s = list(map(int, input().split()))
        s.sort()

        pen = 0
        ans = 0
        time = 0
        for p in s:
            if time + p <= h:
                time += p
                pen += time
                ans += 1

        if i == 0:
            r_ans = ans
            r_pen = pen
        else:
            if ans == r_ans and pen < r_pen:
                pos += 1
            elif ans > r_ans:
                pos += 1
    print(pos)

tc = int(input())
while tc > 0:
    tc -= 1
    sol()
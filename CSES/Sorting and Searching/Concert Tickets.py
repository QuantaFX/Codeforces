from bisect import bisect_right
n, m, = map(int, input().split())
h = sorted(map(int, input().split()))
t = map(int, input().split())

for t_i in t:
    idx = bisect_right(h, t_i)
    if idx == 0:
        print("-1")
    else:
        price_to_pay = h.pop(idx-1)
        print(str(price_to_pay))
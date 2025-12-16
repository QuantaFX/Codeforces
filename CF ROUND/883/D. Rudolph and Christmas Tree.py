def sol():
    n, d, h = map(int, input().split())
    s = list(map(int, input().split()))

    total_area = 0
    area = d/2 * h
    for i in range(n):
        if i == n-1:
            total_area += area
        else:
            area = d/2 * h
            if s[i+1] - s[i] < h:
                n_h = h - s[i+1] + s[i]
                n_d = (d/h) * n_h
                neg_area = n_d / 2 * n_h
                total_area += area - neg_area
            else:
                total_area += area
    print(total_area)

tc = int(input())
while tc > 0:
    tc -= 1
    sol()
def sol():
    n = int(input())
    b = list(map(int, input().split()))
    a = [0] * n

    p_l = 0
    p_r = float('inf')

    for i in range(n // 2):

        sum = b[i]
        l = p_l
        r = sum - l
        if  r > p_r:
            diff =  r - p_r
            l += diff
            r -= diff
        a[i] = l
        a[n - 1 - i] =  r
        p_l = l
        p_r = r

    print(*a)
sol()
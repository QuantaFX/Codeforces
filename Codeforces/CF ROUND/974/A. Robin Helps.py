def sol():
    n, k  = map(int, input().split())
    s = list(map(int, input().split()))

    zero_c = 0
    nums_c = 0

    for i in s:
        if i >= k:
            nums_c += i
        elif i == 0:
            if nums_c > 0:
                nums_c -= 1
                zero_c += 1

    print(zero_c)

tc = int(input())
while tc:
    tc -=1
    sol()
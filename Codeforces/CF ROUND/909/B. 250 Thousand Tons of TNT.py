def sol():
    n = int(input())
    s = list(map(int, input().split()))

    max_diff = max(s) - min(s)

    for i in range(1, n+1):
        if n % i == 0:
            nums = n//i
            a = [0]*nums

            for j in range(n):
                a[j//i] += s[j]

            diff = max(a) - min(a)
            if max_diff < diff:
                max_diff = diff

    print(max_diff)

tc = int(input())
while tc:
    tc -= 1
    sol()
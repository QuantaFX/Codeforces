def sol():
    n = int(input())
    s = list(map(int, input().split()))

    max = min(s)
    for i in range(n):
        m = s[i]
        if m > max:
            max = m
        for j in range(i+1, n):
            if s[j] % 2 != s[j-1] % 2:
                m += s[j]
                if m > max:
                    max = m
            else:
                break
    print(max)

tc = int(input())
while tc:
    tc -= 1
    sol()
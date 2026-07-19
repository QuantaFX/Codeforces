def sol():
    n = int(input())
    s = list(map(int, input().split()))

    odd = 0
    even = 0

    for i in range(n):
        if s[i] % 2 == 0:
            even += 1
        else:
            odd += 1

    if even >= 1:
        print(odd + 1)
    elif odd >= 2:
        print(odd - 1)
    else:
        print(0)

tc = int(input())
while tc:
    tc -= 1
    sol()
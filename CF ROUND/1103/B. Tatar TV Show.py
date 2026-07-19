def sol():
    n, k = map(int, input().split())
    s = input()

    bits = [0] * k

    for i in range(n):
        if s[i] == '1':
            bits[i%k] += 1
    ans = True
    for i in bits:
        if i % 2 != 0:
            ans = False
            break

    if ans:
        print("YES")
    else:
        print("NO")

tc = int(input())
while tc:
    sol()
    tc -= 1
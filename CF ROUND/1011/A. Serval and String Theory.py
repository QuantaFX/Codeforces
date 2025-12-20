def sol():
    n, k = map(int, input().split())
    s = input()

    f = True
    for i in range(1, n):
        if s[i] != s[0]:
            f = False
            break

    if f:
        print("NO")
        return

    if s < s[::-1]:
        print("YES")
    else:
        if k == 0:
            print("NO")
        else:
            print("YES")

tc = int(input())
while tc:
    tc-=1
    sol()
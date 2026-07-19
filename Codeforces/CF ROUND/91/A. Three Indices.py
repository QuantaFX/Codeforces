def sol():
    n = int(input())
    s = list(map(int, input().split()))

    f = True
    for i in range(1, n-1):
        if s[i-1] < s[i] > s[i+1]:
            print("YES")
            print(i, i+1, i+2)
            f = False
            break

    if f:
        print("NO")

tc = int(input())
while tc:
    tc -=1
    sol()
def sol():
    n = int(input())
    s = list(map(int, input().split()))

    if (s[0] == s[-1]):
        print("NO")
    else:
        print("YES")
        print(s[-1], end=" ")
        for i in range(n-1):
            print(s[i], end=" ")
        print()

tc = int(input())
while tc:
    tc -=1
    sol()
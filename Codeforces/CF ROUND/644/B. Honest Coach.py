def sol():
    n = int(input())
    s = list(map(int, input().split()))

    s.sort()

    least = max(s)
    for i in range(n-1):
        if least > s[i+1] - s[i]:
            least = s[i+1] - s[i]
    print(least)

tc = int(input())
while tc:
    tc -=1
    sol()
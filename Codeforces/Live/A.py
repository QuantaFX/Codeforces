def sol():
    n, k = map(int, input().split())
    a = input()

    ans = 0
    for i in range(0, n, k):
        if '0' not in a[i:i+k]:
            ans += 1

    print(ans)

tc = int(input())
while tc:
    tc -= 1
    sol()
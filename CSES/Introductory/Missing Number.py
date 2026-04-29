n = int(input())
a = list(map(int, input().split()))
a.sort()

if a[0] != 1:
    print(1)
else:
    num = 1
    for i in range(1, n-1):
        if a[i] != a[i-1] + 1:
            break
        num += 1
    print(num+1)
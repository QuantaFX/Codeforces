n, m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a = sorted(a)
b = sorted(b)

house, ans = 0, 0
for i in range(len(a)):
    while a[i]+k >= b[house]:
        if a[i]-k <= b[house] <= a[i]+k:
            ans += 1
            house += 1
            break
        house += 1
        if house == len(b):
            break
    if house == len(b):
        break
print(ans)
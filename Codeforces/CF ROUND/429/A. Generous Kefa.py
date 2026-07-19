n, k = map(int, input().split())
s = input()

d = {}
for i in range(n):
    if s[i] in d:
        d[s[i]] += 1
    else:
        d[s[i]] = 1

f = True
for a, b in d.items():
    if b > k:
        f = False
        break

if f:
    print("YES")
else:
    print("NO")
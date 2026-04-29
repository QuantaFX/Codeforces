s = input()

maxi = 1
cur = 1
for i in range(1, len(s)):
    if s[i] == s[i-1]:
        cur += 1
        maxi = max(maxi, cur)
    else:
        cur = 1

print(maxi)
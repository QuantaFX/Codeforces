n = int(input())
s = list(map(int, input().split()))

if n == 2:
    print(0)
else:
    s.sort()
    l = s[n-2] - s[0]
    r = s[n-1] - s[1]
    print(min(l, r))
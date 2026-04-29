import math

n = int(input())
a = list(map(int, input().split()))
freq = [0] * 300001
multiple = [0] * 300001
ans = 0

for c in a:
    ans += multiple[c]

    freq[c] += 1
    div = []
    for d in range(1, int(math.sqrt(c)) + 1):
        if c % d == 0:
            if d != c:
                ans += freq[d]
                div.append(d)
            y = c // d
            if y != d != c:
                ans += freq[y]
                div.append(y)
    print(ans, end=" ")
    div.append(c)
    for d in div:
        multiple[d] += 1
from collections import Counter

def sol():
    n = int(input())
    s = list(map(int, input().split()))

    freq = Counter(s)

    ans = 0
    for count in freq.values():
        if count > 1:
            ans += count * (count - 1) // 2

    if 1 in freq and 2 in freq:
        ans += freq[1] * freq[2]
    print(int(ans))

tc = int(input())
while tc:
    tc -= 1
    sol()
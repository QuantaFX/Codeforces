def sol():
    n, k = map(int, input().split())
    s = list(map(int, input().split()))

    min_dist = min(abs(s[0] - k), abs(s[-1] - k))
    total_dist = s[-1] - s[0]

    print(min_dist + total_dist)


tc = int(input())
while tc:
    tc -=1
    sol()
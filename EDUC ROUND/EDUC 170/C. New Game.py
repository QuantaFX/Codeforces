def sol():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()

    max_cards = 0
    left = 0

    for right in range(n):
        if right > 0 and a[right] - a[right-1] > 1:
            left = right
        while a[right] - a[left] >= k:
            left += 1
        max_cards = max(max_cards, right - left + 1)
    print(max_cards)

tc = int(input())
while tc > 0:
    sol()
    tc -= 1
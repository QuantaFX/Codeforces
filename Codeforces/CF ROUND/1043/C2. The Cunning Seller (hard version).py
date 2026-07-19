melons = [1, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049, 177147, 531441, 1594323, 4782969, 14348907, 43046721, 129140163, 387420489, 1162261467]
deals = [3, 10, 33, 108, 351, 1134, 3645, 11664, 37179, 118098, 373977, 1180980, 3720087, 11691702, 36669429, 114791256, 358722675, 1119214746, 3486784401, 10847773692]

def sol():
    n, k = map(int, input().split())

    ans = [0]*20
    for i in range(19, -1, -1):
        div = n // melons[i]
        if div >= 1:
            ans[i] = div
            n -= melons[i] * div

    deal = sum(ans)
    if k-deal < 0:
        print(-1)
        return

    for i in range(19, 0, -1):
        if ans[i] > 0:
            splits = min(ans[i], (k-deal) // 2)

            ans[i] -= splits
            ans[i-1] += 3 * splits
            deal += 2 * splits

    total_cost = 0
    for i in range(20):
        total_cost += ans[i] * deals[i]
    print(total_cost)

tc = int(input())
while tc:
    tc-=1
    sol()
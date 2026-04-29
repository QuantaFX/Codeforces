MOD = 998244353

# https://stackoverflow.com/questions/11809502/which-is-better-way-to-calculate-ncr
# Taken the approach 1
def ncr(n, r):
    if r > n - r: r = n-r
    ans = 1
    for i in range(1, r+1):
        ans *= (n-r+i)
        ans //= i
    return ans

def npr(n, r):
    if r < 0 or r > n: return 0
    perm = 1
    for i in range(r):
        perm = (perm * (n-i)) % MOD
    return perm

def sol():
    n, a = map(int, input().split())
    secret = list(map(int, input().split()))
    s = input()

    # COUNT THEN REMOVE W
    w = s.count('W')
    s = [c for c in s if c != 'W']

    # s is empty (ALl W) just Permutations
    # G should be the start
    if not s:
        print(npr(a-n, w))
        return
    elif s[0] == 'Y':
        print("0")
        return

    # G COUNT, Y COUNT
    g = s.count('G')
    y = s.count('Y')

    # Right to Left counts of Y's after placing G's
    cap = [0] * (g + 1)
    y_count = 0
    g_placed = 0
    for char in reversed(s):
        if char == 'Y':
            y_count += 1
        elif char == 'G':
            g_placed += 1
            cap[g_placed] = y_count

    # i = G's processed
    # j = Y's processed
    dp = [[0] * (y+1) for _ in range(g+1)]
    dp[0][0] = 1

    for i in range(g+1):
        max_y = cap[i]
        if y < max_y:
            max_y = y
        for j in range(max_y+1):
            if dp[i][j] == 0:
                continue
            if i < g:
                dp[i+1][j] = (dp[i+1][j]+dp[i][j]) % MOD
            if j < cap[i]:
                dp[i][j+1] = (dp[i][j+1] + dp[i][j] * (cap[i]-j)) % MOD

    ans = dp[g][y]
    ans = (ans * ncr(n, g+y)) % MOD
    ans = (ans * npr(a-n, w)) % MOD
    print(ans)

tc = int(input())
while tc:
    tc-=1
    sol()
n, q = map(int, input().split())

num = list(map(int, input().split()))
tree = [0] * (2 * n)

for i in range(n):
    tree[n+i] = num[i]

for i in range(n-1, 0, -1):
    tree[i] = min(tree[2 * i], tree[2 * i + 1])

for i in range(q):
    a, b = map(int, input().split())

    l = a - 1 + n
    r = b - 1 + n
    ans = float('inf')

    while l <= r:
        if l % 2 == 1:
            if tree[l] < ans:
                ans = tree[l]
            l += 1

        if r % 2 == 0:
            if tree[r] < ans:
                ans = tree[r]
            r -= 1

        l //= 2
        r //= 2

    print(ans)
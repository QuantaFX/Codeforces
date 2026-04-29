n = int(input())
a = list(map(int, input().split()))

adj = [[] for i in range(n+1)]

for i in range(2, n+1):
    adj[a[i-2]].append(i)

count = [-1] * (n+1)

for i in range(1, n+1):
    add = 0
    for v in adj[i]:
        add += 1

import sys
sys.setrecursionlimit(100000)

n, m = map(int, input().split())
adj = [[] for _ in range(n+1)]
visit = [False for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

def dfs(v):
    visit[v] = True
    for u in adj[v]:
        if not visit[u]:
            dfs(u)

count = 0
ans = []
for i in range(1, n+1):
    if visit[i]:
        continue
    else:
        count += 1
        ans.append(i)
        dfs(i)

print(count-1)
for i in range(len(ans)-1):
    print(ans[i], ans[i+1])
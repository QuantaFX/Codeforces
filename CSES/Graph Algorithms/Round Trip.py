import sys
sys.setrecursionlimit(100000)

n, m = map(int, input().split())

adj = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

visited = [False] * (n + 1)
parent = [0] * (n + 1)

found = False
def dfs(u, p):
    global found
    visited[u] = True
    parent[u] = p

    for v in adj[u]:
        if v == p:
            continue
        if visited[v]:
            found = True
            cycle = []
            curr = u
            while curr != v:
                cycle.append(curr)
                curr = parent[curr]

            print(len(cycle) + 2)
            print(v, end=" ")
            print(*cycle, end=" ")
            print(v)

            return True
        if dfs(v, u):
            return True
    return False

for i in range(1, n + 1):
    if not visited[i]:
        if dfs(i, 0):
            break

if not found:
    print("IMPOSSIBLE")
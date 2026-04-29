from collections import deque

n, m = map(int, input().split())

adj = [[] for _ in range(n+1)]
dist = [-1 for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

def bfs(start, end):
    q = deque([start])
    dist[start] = 1

    while q:
        s = q.popleft()
        for d in adj[s]:
            if dist[d] == -1 or dist[d] > dist[s] + 1:
                dist[d] = dist[s] + 1
                q.append(d)

nodes = [n]
def backtrack(start, end):
    q = deque([end])
    while q:
        s = q.popleft()
        if s == start:
            return
        for d in adj[s]:
            if dist[d] == dist[s]-1:
                nodes.append(d)
                q.append(d)
                break

bfs(1, n)

if dist[n] == -1:
    print("IMPOSSIBLE")
else:
    print(dist[n])
    backtrack(1, n)
    print(*nodes[::-1])

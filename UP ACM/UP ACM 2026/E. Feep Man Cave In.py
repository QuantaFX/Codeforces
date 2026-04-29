from collections import deque

def sol():
    n, m = map(int, input().split())
    adj = [[] for _ in range(n+1)]

    for i in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

    a, b, h = map(int, input().split())

    dist = [0] + [-1] * n
    dist[h] = 0
    q = deque([h])

    # BFS TRAVERSE AND ADD DIST FROM H
    while q:
        curr = q.popleft()
        for node in adj[curr]:
            if dist[node] == -1:
                dist[node] = dist[curr] + 1
                q.append(node)

    # UNION FIND
    parent = list(range(n+1))
    nodes = sorted(range(1, n+1), key=lambda x: dist[x], reverse=True)

    def find(i):
        if parent[i] != i:
            parent[i] = find(parent[i])
        return parent[i]

    def union(a, b):
        start = find(a)
        end = find(b)
        if start != end:
            parent[start] = end

    linked = [0] * (n+1)

    for start in nodes:
        linked[start] = 1

        for end in adj[start]:
            if linked[end]:
                union(start, end)

        if find(a) == find(b):
            print(dist[start])
            return

sol()
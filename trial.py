import itertools

def get_unique_trees():
    edges = [(1,2),(2,3),(4,5),(5,6),(7,8),(8,9),(1,4),(2,5),(3,6),(4,7),(5,8),(6,9)]
    rot = {1:3, 2:6, 3:9, 4:2, 5:5, 6:8, 7:1, 8:4, 9:7}
    flip = {1:3, 2:2, 3:1, 4:6, 5:5, 6:4, 7:9, 8:8, 9:7}

    def get_orbit(tree):
        orbit = set()
        curr = tree
        for _ in range(4):
            curr = tuple(sorted([tuple(sorted((rot[u], rot[v]))) for u,v in curr]))
            orbit.add(curr)
            f_curr = tuple(sorted([tuple(sorted((flip[u], flip[v]))) for u,v in curr]))
            orbit.add(f_curr)
        return orbit

    def is_tree(combo):
        adj = {i: [] for i in range(1, 10)}
        for u, v in combo:
            adj[u].append(v); adj[v].append(u)
        vstd, stack = {1}, [1]
        while stack:
            curr = stack.pop()
            for n in adj[curr]:
                if n not in vstd: vstd.add(n); stack.append(n)
        return len(vstd) == 9

    labeled = [tuple(sorted(c)) for c in itertools.combinations(edges, 8) if is_tree(c)]
    unique, seen = [], set()
    for t in labeled:
        if t not in seen:
            unique.append(t)
            seen.update(get_orbit(t))
    return unique

def render(tree_edges):
    edge_set = set(tree_edges)
    glyphs = {
        (0,0,0,0): ' ', (0,0,0,1): '╶', (0,0,1,0): '╴', (0,0,1,1): '─',
        (0,1,0,0): '╷', (0,1,0,1): '┌', (0,1,1,0): '┐', (0,1,1,1): '┬',
        (1,0,0,0): '╵', (1,0,0,1): '└', (1,0,1,0): '┘', (1,0,1,1): '┴',
        (1,1,0,0): '│', (1,1,0,1): '├', (1,1,1,0): '┤', (1,1,1,1): '┼'
    }
    res = []
    for r in range(3):
        row = ""
        for c in range(3):
            n = r * 3 + c + 1
            U = tuple(sorted((n, n-3))) in edge_set if r > 0 else 0
            D = tuple(sorted((n, n+3))) in edge_set if r < 2 else 0
            L = tuple(sorted((n, n-1))) in edge_set if c > 0 else 0
            R = tuple(sorted((n, n+1))) in edge_set if c < 2 else 0
            row += glyphs[(U,D,L,R)]
        res.append(row)
    return "\n".join(res)


trees = get_unique_trees()
for i, t in enumerate(trees):
    print(f"#{i+1}\n{render(t)}\n")
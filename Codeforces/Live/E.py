from bisect import bisect_left

def sol():
    n = int(input())
    parts = []
    for i in range(n):
        a, b = map(int, input().split())
        parts.append((a, b))

    m = int(input())
    actors = []
    total_capacity = 0
    for i in range(m):
        c, d, k = map(int, input().split())
        actors.append((c, d, k))
        total_capacity += k

    if total_capacity < n:
        print("NO")
        return

    events = []
    for i in range(n):
        events.append((parts[i][0], 1, parts[i][1], i + 1))
    for i in range(m):
        events.append((actors[i][0], 0, actors[i][1], actors[i][2], i + 1))

    events.sort()
    unique_d = sorted(list(set(a[1] for a in actors)))
    U_orig = len(unique_d)

    if U_orig == 0:
        if n > 0:
            print("NO")
        return

    U = 1
    while U < U_orig:
        U *= 2

    tree = bytearray(2 * U)
    leaf_lists = [[] for _ in range(U_orig)]
    ans = [0] * (n + 1)

    for ev in events:
        if ev[1] == 0:
            _, _, d, k, actor_idx = ev
            comp_d = bisect_left(unique_d, d)
            leaf_lists[comp_d].append([k, actor_idx])

            if len(leaf_lists[comp_d]) == 1:
                pos = U + comp_d
                tree[pos] = 1
                pos //= 2
                while pos > 0:
                    tree[pos] = tree[2 * pos] | tree[2 * pos + 1]
                    pos //= 2
        else:
            _, _, b, part_idx = ev
            comp_b = bisect_left(unique_d, b)

            if comp_b == U_orig:
                print("NO")
                return

            ql, qr = comp_b, U_orig - 1
            l, r = ql + U, qr + U
            left_nodes, right_nodes = [], []

            while l <= r:
                if l % 2 == 1:
                    left_nodes.append(l)
                    l += 1
                if r % 2 == 0:
                    right_nodes.append(r)
                    r -= 1
                l //= 2
                r //= 2

            found_node = -1
            for node in left_nodes:
                if tree[node] == 1:
                    found_node = node
                    break
            if found_node == -1:
                for node in reversed(right_nodes):
                    if tree[node] == 1:
                        found_node = node
                        break

            if found_node == -1:
                print("NO")
                return

            curr = found_node
            while curr < U:
                if tree[2 * curr] == 1:
                    curr = 2 * curr
                else:
                    curr = 2 * curr + 1

            comp_found = curr - U
            ans[part_idx] = leaf_lists[comp_found][-1][1]

            leaf_lists[comp_found][-1][0] -= 1
            if leaf_lists[comp_found][-1][0] == 0:
                leaf_lists[comp_found].pop()
                if len(leaf_lists[comp_found]) == 0:
                    pos = U + comp_found
                    tree[pos] = 0
                    pos //= 2
                    while pos > 0:
                        tree[pos] = tree[2 * pos] | tree[2 * pos + 1]
                        pos //= 2

    print("YES")
    print(" ".join(map(str, ans[1:])))

sol()
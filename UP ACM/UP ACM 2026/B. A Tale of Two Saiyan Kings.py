n = int(input())
k1, k2, k = map(int, input().split())

li = [[] for _ in range(n+1)]

for i in range(n):
    c = list(map(int, input().split()))
    li[i+1] = c[1:]

print(*li)

visited1 = set()
visited2 = set()

def inorder(val, visited):
    global found, k

    if val in visited:
        return
    visited.add(val)

    curr = li[val]

    if found or val == k:
        if val == k:
            found = True
        return

    for j in range(len(curr)):
        if not found:
            inorder(curr[j], visited)

found = False
inorder(k1, visited1)
found = False
inorder(k2, visited2)

if k in visited1 and k in visited2:
    ans = visited1 | visited2
    print(len(ans)-1)
else:
    print("IMPOSSIBLE")
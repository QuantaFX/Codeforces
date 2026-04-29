from collections import deque

n, m = map(int, input().split())

adj = [[] for _ in range(n+1)]
number = [-1 for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

def bfs(start):
    q = deque([start])
    number[start] = 1

    while q:
        s = q.popleft()
        for d in adj[s]:
            if number[d] == -1:
                number[d] = number[s] % 2 + 1
                q.append(d)
            elif number[d] == number[s]:
                return False
    return True

flag = False
for i in range(1, n+1):
    if number[i] == -1:
        if not bfs(i):
            flag = True
            break

if not flag:
    print(*number[1:])
else:
    print("IMPOSSIBLE")
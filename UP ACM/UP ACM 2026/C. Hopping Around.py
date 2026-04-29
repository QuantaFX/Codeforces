from collections import deque

def bfs(arr, start, end, rows, cols, portals):
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # 4 directions
    dist = [[-1] * cols for _ in range(rows)]

    sx, sy = start
    dist[sx][sy] = 0
    q = deque([start])
    used_portals = set()

    while q:
        i, j = q.popleft()

        if (i, j) == end:
            return dist[i][j]

        curr = arr[i][j]
        if 'A' <= curr <= 'Z' and curr not in used_portals:
            for pr, pc in portals[curr]:
                if dist[pr][pc] == -1 or dist[pr][pc] > dist[i][j]:
                    dist[pr][pc] = dist[i][j]
                    q.appendleft((pr, pc))
            used_portals.add(curr)

        for dx, dy in moves:
            ni, nj = i + dx, j + dy
            if 0 <= ni < rows and 0 <= nj < cols and arr[ni][nj] != '#':
                if dist[ni][nj] == -1 or dist[ni][nj] > dist[i][j] + 1:
                    dist[ni][nj] = dist[i][j] + 1
                    q.append((ni, nj))

    return "-1"

cols = rows = int(input())
arr = [list(input().strip()) for _ in range(rows)]
portals = {chr(i): [] for i in range(ord('A'), ord('Z')+1)}
start = end = None

for i in range(rows):
    for j in range(cols):
        char = arr[i][j]
        if char == '@':
            start = (i, j)
        elif char == '!':
            end = (i, j)
        elif 'A' <= char <= 'Z':
            portals[char].append((i, j))

print(bfs(arr, start, end, rows, cols, portals))

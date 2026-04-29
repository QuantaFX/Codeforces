from collections import deque

moves = [(-1, 0, 'D'), (1, 0, 'U'), (0, -1, 'R'), (0, 1, 'L')]

rows, cols = map(int, input().split())
room = [list(input().strip()) for _ in range(rows)]
dist = [[-1] * cols for _ in range(rows)]

movement = []

def bfs(start, end):
    q = deque([start])

    while q:
        x, y = q.popleft()
        if (x, y) == end:
            return
        for dx, dy, dire in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and room[nx][ny] != '#':
                if dist[nx][ny] == -1 or dist[nx][ny] > dist[x][y] + 1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))

def backtrack(start, end):
    q = deque([end])

    while q:
        x, y = q.popleft()
        if (x, y) == start:
            return
        for dx, dy, dire in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                if dist[nx][ny] == dist[x][y] - 1:
                    movement.append(dire)
                    q.append((nx, ny))
                    break

start = end = None
for i in range(rows):
    for j in range(cols):
        if room[i][j] == 'A':
            dist[i][j] = 0
            start = (i, j)
        elif room[i][j] == 'B':
            end = (i, j)

bfs(start, end)
if dist[end[0]][end[1]] == -1:
    print("NO")
else:
    print("YES")
    print(dist[end[0]][end[1]])
    backtrack(start, end)
    for i in movement[::-1]:
        print(i, end='')

from collections import deque

rows, cols = map(int, input().split())
room = [list(input().strip()) for _ in range(rows)]
count = 0
def bfs(x, y):
    q = deque((x, y))
    while q:
        x, y = q.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx,y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                if room[nx][ny] == '.':
                    room[nx][ny] = "#"
                    q.append((nx, ny))

for i in range(rows):
    for j in range(cols):
        if room[i][j] == '.':
            count += 1
            bfs(i, j)

print(count)

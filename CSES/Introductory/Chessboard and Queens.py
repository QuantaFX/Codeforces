grid = [input() for i in range(8)]
cols, backward, forward =  [0] * 8, [0] * 15, [0] * 15
answer = 0
def sol(r):
    if r == 8:
        global answer
        answer += 1
        return
    for c in range(8):
        if grid[r][c] == '.' and not cols[c] and not backward[r-c+7] and not forward[r+c]:
            cols[c] = backward[r-c+7] = forward[r+c] = 1
            sol(r+1)
            cols[c] = backward[r-c+7] = forward[r+c] = 0
sol(0)
print(answer)
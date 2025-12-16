def sol():
    board = []
    for i in range(3):
        board.append(list(input()))

    win = "lose"
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != '.':
            win = board[i][0]
            break
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != '.':
            win = board[0][i]
            break

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '.':
        win = board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '.':
        win = board[0][2]

    if win == "lose":
        print("DRAW")
    else:
        print(win)

tc = int(input())
while tc > 0:
    tc -= 1
    sol()
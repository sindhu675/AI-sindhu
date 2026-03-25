# Simple Tic Tac Toe

board = [" "] * 9
player = "X"

for i in range(9):
    print(board[0:3])
    print(board[3:6])
    print(board[6:9])

    pos = int(input("Enter position (1-9): ")) - 1

    if board[pos] == " ":
        board[pos] = player
        if player == "X":
            player = "O"
        else:
            player = "X"
    else:
        print("Already filled")

print("Game Over")

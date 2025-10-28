from memory.game import create_board

board_game= create_board(10)
for i in board_game:
    for j in i:
        print(j, end=" ")
    print()

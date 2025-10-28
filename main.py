from memory.game import create_board, create_pairs

board_game = create_board(4)
for i in board_game:
    for j in i:
        print(j, end=" ")
    print()

print(create_pairs(4))


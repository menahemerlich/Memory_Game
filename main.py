from memory.game import create_board, create_pairs, board_with_pairs, random_mixing
size = 4
board_game = create_board(size)
card_list = create_pairs(size)
card_list_2 = random_mixing(card_list)
board_game_2 = board_with_pairs(board_game, card_list)
for i in board_game_2:
    for j in i:
        print(j, end=" ")
    print()




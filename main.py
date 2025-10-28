from memory.game import create_board, create_pairs, board_with_pairs, random_mixing
from memory.io import input_coordinates, test_input

size = 8
game_board_display = create_board(size)
card_list = random_mixing(create_pairs(size))
game_board_indoor = board_with_pairs(create_board(size), card_list)

for i in game_board_display:
     for j in i:
         print(j, end="  ")
     print()

print()
for i in game_board_indoor:
     for j in i:
         print(j, end="  ")
     print()



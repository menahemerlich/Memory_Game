from memory.game import create_board, create_pairs, board_with_pairs, random_mixing
from memory.io import input_coordinates, test_input, input_conver, correct_pairs_list, change_board

size = 4
game_board_display = create_board(size)
card_list = random_mixing(create_pairs(size))
game_board_indoor = board_with_pairs(create_board(size), card_list)
coordinates = input_coordinates()
while not test_input(coordinates, size, correct_pairs=[["2", "5"]]):
    coordinates = input_coordinates()
input_conver(coordinates)
print(correct_pairs_list(game_board_indoor, coordinates_1=[0, 0], coordinates_2=[2, 0]))
change_board(game_board_display, game_board_indoor, coordinates)

for i in game_board_display:
     for j in i:
         print(f"{j:3}", end="  ")
     print()

print()
for i in game_board_indoor:
     for j in i:
         print(f"{j:3}", end="  ")
     print()



from memory.game import create_board, create_pairs, board_with_pairs, random_mixing
from memory.io import input_coordinates, test_input, input_conver, correct_pairs_list, change_board_temporary, change_board, if_finished, test_correct_pairs

size = 2
correct_pairs = []
coordinates_list = []
game_board_display = create_board(size)
card_list = random_mixing(create_pairs(size))
game_board_indoor = board_with_pairs(create_board(size), card_list)

for i in game_board_display:
    for j in i:
        print(f"{j:3}", end="  ")
    print()
while not if_finished(game_board_display):
    coordinates = input_coordinates()
    while not test_input(coordinates, size) and test_correct_pairs(correct_pairs, coordinates):
        coordinates = input_coordinates()
    coordinates = input_conver(coordinates)
    coordinates_list.append(coordinates)
    if len(coordinates_list) <= 1:
        change_board_temporary(game_board_display, game_board_indoor, coordinates)
    elif len(coordinates_list) == 2:
        if change_board(game_board_display, game_board_indoor, coordinates_list[0], coordinates_list[1])[0]:
            correct_pairs.append(coordinates_list[0])
            correct_pairs.append(coordinates_list[1])
            coordinates_list = []
            for i in game_board_display:
                 for j in i:
                     print(f"{j:3}", end="  ")
                 print()
        else:
            change_board_temporary(game_board_display, game_board_indoor, coordinates)
            coordinates_list = []

print("Finish!!!!!")
for i in game_board_display:
    for j in i:
        print(f"{j:3}", end="  ")
    print()





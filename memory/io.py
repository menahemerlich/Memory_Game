correct_pairs = []
def input_coordinates():
    global coordinates
    choice = input("Enter your coordinates: ")
    coordinates = choice.split(" ")
    return coordinates

def test_input(coordinates: list[str], size:int, correct_pairs:list[list[str]]):
    if coordinates[0].isnumeric() and coordinates[-1].isnumeric() and coordinates not in correct_pairs:
        if int(coordinates[0]) < size and int(coordinates[-1]) < size and len(coordinates) == 2:
            return True
    return False

def input_conver(coordinates:list[str]):
    for i in range(len(coordinates)):
        coordinates[i] = int(coordinates[i])
    return coordinates

def correct_pairs_list(board: list[list[int]], coordinates_1:list[int], coordinates_2:list[int]):
    global correct_pairs
    if board[coordinates_1[0]][coordinates_1[1]] == board[coordinates_2[0]][coordinates_2[1]]:
        correct_pairs.append(coordinates_1)
    return correct_pairs

def change_board_temporary(board_1: list[list[int]], board_2: list[list[int]],coordinates: list[int]):
    temporary = board_1[coordinates[0]][coordinates[1]]
    board_1[coordinates[0]][coordinates[1]] = board_2[coordinates[0]][coordinates[1]]
    for i in board_1:
        for j in i:
            print(f"{j:3}", end="  ")
        print()
    print()
    board_1[coordinates[0]][coordinates[1]] = temporary
    return board_1

def change_board(board_1: list[list[int]], board_2: list[list[int]], coordinates_1:list[int], coordinates_2:list[int]):
    if board_2[coordinates_1[0]][coordinates_1[1]] == board_2[coordinates_2[0]][coordinates_2[1]]:
        board_1[coordinates_1[0]][coordinates_1[1]] = board_2[coordinates_1[0]][coordinates_1[1]]
        board_1[coordinates_2[0]][coordinates_2[1]] = board_2[coordinates_2[0]][coordinates_2[1]]
    return board_1

def if_finished(board_1: list[list[int]]):
    for i in board_1:
        if "x" in i:
            return False
    return True



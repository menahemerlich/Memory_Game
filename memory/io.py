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





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








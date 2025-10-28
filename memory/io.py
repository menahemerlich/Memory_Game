correct_pairs = [["2", "5"]]
def input_coordinates():
    global coordinates
    choice = input("Enter your coordinates: ")
    coordinates = choice.split(" ")
    return coordinates

def test_input(coordinates: list[str], size:int, correct_pairs):
    for i in coordinates:
        if i.isnumeric() and coordinates not in correct_pairs and len(coordinates) == 2:
            if int(i) < size and int(coordinates[-1]) < size:
                return True
    return False






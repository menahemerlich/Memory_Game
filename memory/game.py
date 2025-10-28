import random

def create_board(size: int, fill:str = "x"):
    board = []
    if (size ** 2) % 2 == 0:
        for i in range(size):
            board.append([])
            for j in range(size):
                board[i].append(fill)
    return board


def create_pairs(size:int):
    card_number = []
    for i in range(0, (size ** 2) // 2):
        card_number.append(i + 1)
    return card_number

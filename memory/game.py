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
    card_list = []
    for i in range(1, ((size ** 2) // 2) + 1):
        card_list.append(i)
        card_list.append(i)
    return card_list

def random_mixing(card_list: list[int]):
    for i in range(50):
        index1 = random.randint(0, len(card_list) - 1)
        index2 = random.randint(0, len(card_list) - 1)
        if index1 != index2:
            card_list[index1], card_list[index2] = card_list[index2], card_list[index1]
    return card_list

def board_with_pairs(board: list[list[int]] ,card_list: list[int]):
    for i in range(len(board)):
        for j in range(len(board[i])):
            mix_card = card_list.pop(0)
            board[i][j] = mix_card
    return board






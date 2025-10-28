
def create_board(size: int, fill:str = "x"):
    board = []
    for i in range(size):
        board.append([])
        for j in range(size):
            board[i].append(fill)
    return board
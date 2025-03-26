arr = []
for x in range(3):
    row = []
    for y in range(3):
        row.append(0)
    arr.append(row)


class game:

    def __init__(self):
            self.player1 = player("Player 1", "X")
            self.player2 = player("Player 2", "O")
            self.turn = player1
            self.board = board()

    def change_turn(self):
        if self.turn == player1:
            self.turn = player2
        else:
            self.turn = player1



class player:

    def __init__(self):
        self.name = name
        self.shape = shape


    def move(self):
        choice = int(input("Enter the number 1-9: "))
        board[choice - 1] == self.shape
        print(board)



class board:


    def __init__(self):
        self.array = arr


    def is_full(self):

        for row in arr:
            if row == '':
                return False
            else:
                return True



    def fill(self, row, collumn, shape):

        if self.array[row][collumn] == '':
            self.array[row][collumn] = shape
            return True
        else:
            return False

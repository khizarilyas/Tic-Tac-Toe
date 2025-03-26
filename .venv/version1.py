
array = []
for x in range(3):
    row = []
    for y in range(3):
        row.append('-')
    array.append(row)


def win_x(arr):
    if arr[0][0] == arr[0][1] == arr[0][2] == 'X':
        return True
    elif arr[1][0] == arr[1][1] == arr[1][2] == 'X':
        return True
    elif arr[2][0] == arr[2][1] == arr[2][2] == 'X':
        return True
    elif arr[0][0] == arr[1][0] == arr[2][0] == 'X':
        return True
    elif arr[0][1] == arr[1][1] == arr[2][1] == 'X':
        return True
    elif arr[0][2] == arr[1][2] == arr[2][2] == 'X':
        return True
    elif arr[0][0] == arr[1][1] == arr[2][2] == 'X':
        return True
    elif arr[0][2] == arr[1][1] == arr[2][0] == 'X':
        return True
    else:
        return False


def win_o(arr):
    if arr[0][0] == arr[0][1] == arr[0][2] == 'O':
        return True
    elif arr[1][0] == arr[1][1] == arr[1][2] == 'O':
        return True
    elif arr[2][0] == arr[2][1] == arr[2][2] == 'O':
        return True
    elif arr[0][0] == arr[1][0] == arr[2][0] == 'O':
        return True
    elif arr[0][1] == arr[1][1] == arr[2][1] == 'O':
        return True
    elif arr[0][2] == arr[1][2] == arr[2][2] == 'O':
        return True
    elif arr[0][0] == arr[1][1] == arr[2][2] == 'O':
        return True
    elif arr[0][2] == arr[1][1] == arr[2][0] == 'O':
        return True
    else:
        return False


def output(arr):
    for row in arr:
        print(row)


def is_full(arr):
    for i in arr:
        for cell in i:
            if cell == '-':
                return False
    return True


var = is_full(array)

output(array)
x
while not var:

    p1_x = int(input("Player 1 enter the row: "))
    p1_y = int(input("Player 1 enter the column: "))

    while array[p1_x - 1][p1_y - 1] != '-':

        output(array)
        print("That space is taken enter new space please")
        p1_x = int(input("Player 1 enter the row: "))
        p1_y = int(input("Player 1 enter the column: "))

    array[p1_x - 1][p1_y - 1] = "X"
    output(array)

    if win_x(array):
        var = True

    if not var and not is_full(array):

        p2_x = int(input("Player 2 enter the row: "))
        p2_y = int(input("Player 2 enter the column: "))

        while array[p2_x - 1][p2_y - 1] != '-' and not var:

            if is_full(array):
                var = True
            else:
                output(array)
                print("That space is taken enter new space please")
                p2_x = int(input("Player 2 enter the row: "))
                p2_y = int(input("Player 2 enter the column: "))

        if not is_full(array):
            array[p2_x - 1][p2_y - 1] = "O"
            output(array)
        else:
            var = True
        if win_o(array):
            var = True


    else:
        if win_x(array):
            print("Player 1 wins!!!")
            var = True

        elif win_o(array):
            print("Player 2 wins!!!")
            var = True

        else:
            print("It's a draw. Better luck next time.")
            var = True



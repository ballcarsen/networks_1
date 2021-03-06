

# Reads in the board from a text file, returns the array representing the board
def read_board(file_name):
    with open(file_name) as file:
        next(file) #skips first row of the file since its all numbers anyway
        board_array = [line.split() for line in file]
        return board_array


# Saves the board to the text file
def save_board(file_name, board_array):
    with open(file_name, "w") as f:
        f.write("  0 1 2 3 4 5 6 7 8 9")
        for r in board_array:
            f.write("\n")
            for c in r:
                f.write(str(c) + " ")


# Checks to see what is at the board at the given coordinates, returns the corresponding information
def check_board(x, y, board_array):
    char_at_pos = board_array[y][x+1]
    if char_at_pos == '_':
        board_array[y][x+1] = "O"
        return [board_array, 200, 0]
    elif char_at_pos == 'X' or char_at_pos == "O":
        return [board_array, 410]
    else:
        board_array[y][x+1] = "X"
        count = sum(x.count("X") for x in board_array)
        print(count)
        if count == 17:
            return [board_array, 200, 1, char_at_pos, True]
        else:
            if sum(x.count(char_at_pos) for x in board_array) == 0:
                return [board_array, 200, 1, char_at_pos]
            else:
                return [board_array, 200, 1]


# Sets the character at x, y to the given character
def update_board(x, y,  board_array, character):
    board_array[y][x+1] = character
    return board_array

# Processes a request from the server or client to handle
def process_request(x, y, file_name, character = None):
    board_array = read_board(file_name)
    #Changes the character at position x,y
    if character:
        board_array = update_board(x,y, board_array, character)
        save_board(file_name, board_array)
        return(True)
    # checks the board to see what exists at the given coordinates and returns the corresponding information
    else:
        results = check_board(x, y, board_array)
        save_board(file_name, results[0])
        return results[1:]

if __name__ == '__main__':
    print(process_request(1, 1, 'own_board.txt'))











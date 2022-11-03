def valid_line(line):
    if 0 in line:
        return False
    return (len(line) == 9 and sum(line) == sum(set(line)))

def get_column(matrix, i):
    return [row[i] for row in matrix]

def main(board):
    validation = []
    for row in board:
        validation.append(valid_line(row))
    for i in range(9):
        validation.append(valid_line(get_column(board, i)))
    if False in validation:
        return "Try again!"
    else:
        return "Finished!"

def miner_locations(maze: list):
    miner_location = \
        [[row, column] for column in range(len(maze)) for row in range(len(maze)) if matrix[row][column] == 's']
    mrow, mcolumn = miner_location[0]
    return mrow, mcolumn


matrix_size = int(input())
miner_moves = input().split()
matrix = [[char for char in input().split(' ')] for row in range(matrix_size)]

game_over = False
collected_all_coals = False

miner_row = 0
miner_column = 0
total_coal = 0

for move in miner_moves:
    miner_row, miner_column = miner_locations(matrix)
    if move == 'up' and miner_row > 0:
        if matrix[miner_row - 1][miner_column] == 'e':
            game_over = True
        matrix[miner_row][miner_column] = '*'
        matrix[miner_row - 1][miner_column] = 's'
    elif move == 'down' and miner_row < matrix_size - 1:
        if matrix[miner_row + 1][miner_column] == 'e':
            game_over = True
        matrix[miner_row][miner_column] = '*'
        matrix[miner_row + 1][miner_column] = 's'
    elif move == 'left' and miner_column > 0:
        if matrix[miner_row][miner_column - 1] == 'e':
            game_over = True
        matrix[miner_row][miner_column] = '*'
        matrix[miner_row][miner_column - 1] = 's'
    elif move == 'right' and miner_column < matrix_size - 1:
        if matrix[miner_row][miner_column + 1] == 'e':
            game_over = True
        matrix[miner_row][miner_column] = '*'
        matrix[miner_row][miner_column + 1] = 's'
    total_coal = 0
    for row in matrix:
        for el in row:
            if el == 'c':
                total_coal += 1
    if total_coal == 0:
        collected_all_coals = True
    if game_over:
        break
    if collected_all_coals:
        break

miner_row, miner_column = miner_locations(matrix)
if game_over:
    print(f"Game over! ({miner_row}, {miner_column})")
elif collected_all_coals:
    print(f"You collected all coal! ({miner_row}, {miner_column})")
else:
    print(f"{total_coal} pieces of coal left. ({miner_row}, {miner_column})")

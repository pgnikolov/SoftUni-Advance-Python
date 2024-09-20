rows, cols = map(int, input().split())
matrix = [[' ' for _ in range(cols)] for _ in range(rows)]

snake = [char for char in input()]
current_char = ''

for row in range(rows):
    if row % 2 == 0:
        start_col = 0
        end_col = cols
        move = 1
    else:
        start_col = cols - 1
        end_col = -1
        move = -1
    for column in range(start_col, end_col, move):
        current_char = snake.pop(0)
        snake.append(current_char)
        matrix[row][column] = current_char

for row in matrix:
    print("".join(row))

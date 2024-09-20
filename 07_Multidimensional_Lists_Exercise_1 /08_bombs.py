n = int(input())
matrix = [[int(x) for x in input().split(' ')] for row in range(n)]
bombs_list = [[int(coordinate) for coordinate in info.split(',')] for info in input().split()]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1), (0, 0)]

alive_cell = 0
total_sum = 0

for row_bomb, column_bomb in bombs_list:
    bomb_dmg = matrix[row_bomb][column_bomb]
    if bomb_dmg < 1:
        continue
    for x, y in directions:
        current_row, current_col = row_bomb + x, column_bomb + y
        if 0 <= current_row < n and 0 <= current_col < n:
            matrix[current_row][current_col] -= bomb_dmg if matrix[current_row][current_col] > 0 else 0

alive_cell = [num for row_cell in matrix for num in row_cell if int(num > 0)]

print(f'Alive cells: {len(alive_cell)}')
print(f'Sum: {sum(alive_cell)}')
[print(*row_print) for row_print in matrix]

rows, cols = map(int, input().split(', '))

matrix = [[row for row in input().split(', ')] for _ in range(rows)]
max_sum_small_matrix= 0
small_matrix_max = []

for row in range(rows - 1):
    for col in range(cols - 1):
        current_sum = 0
        current_matrix = []
        for sub_row in range(row, row + 2):
            sub_current_matrix = []
            for sub_col in range(col, col + 2):
                sub_current_matrix.append(int(matrix[sub_row][sub_col]))
                current_sum += int(matrix[sub_row][sub_col])
            current_matrix += [sub_current_matrix]

        if current_sum > max_sum_small_matrix:
            max_sum_small_matrix = current_sum
            small_matrix_max = current_matrix

for row in small_matrix_max:
    print(*row)

print(max_sum_small_matrix)

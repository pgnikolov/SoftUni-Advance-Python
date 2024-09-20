row, cols = map(int, input().split())

matrix = [[char for char in input().split()] for _ in range(row)]
counter = 0

for i in range(row - 1):
    for j in range(cols - 1):
        # matrix_2_2 = [[matrix[i][j], matrix[i][j + 1]], [matrix[i + 1][j], matrix[i + 1][j + 1]]]
        # print(matrix_2_2)
        if matrix[i][j] == matrix[i][j + 1] == matrix[i + 1][j] == matrix[i + 1][j + 1]:
            counter += 1

print(counter)

rows, cols = map(int, input().split(', '))
matrix = []

for i in range(rows):
    matrix.append(list(map(int, input().split())))

for i in range(cols):
    sum_col = 0
    for j in range(rows):
        sum_col += matrix[j][i]
    print(sum_col)

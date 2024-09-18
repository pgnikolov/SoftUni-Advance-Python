rows, cols = map(int, input().split(', '))

matrix = []
for i in range(rows):
    matrix.append([int(num) for num in input().split(", ")])

total_sum = 0
for i in range(rows):
    for j in range(cols):
        total_sum += matrix[i][j]

print(total_sum)
print(matrix)

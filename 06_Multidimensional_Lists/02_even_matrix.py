rows = int(input())
matrix = []

for _ in range(rows):
    row = map(int, input().split(', '))
    matrix.append(row)


even_matrix = [[num for num in row if num % 2 == 0] for row in matrix]
print(even_matrix)

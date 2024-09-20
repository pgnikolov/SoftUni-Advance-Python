rows = int(input())
primary_diagonal = 0
secondary_diagonal = 0

matrix = [[int(num) for num in input().split(', ')] for _ in range(rows)]

primary_diagonal_els = []
secondary_diagonal_els = []

for i in range(len(matrix)):
    primary_diagonal += matrix[i][i]
    primary_diagonal_els.append(str(matrix[i][i]))
    secondary_diagonal += matrix[i][rows - i - 1]
    secondary_diagonal_els.append(str(matrix[i][rows - i - 1]))

print(
    f"Primary diagonal: {', '.join(primary_diagonal_els)}. Sum: {primary_diagonal}\nSecondary diagonal:"
    f" {', '.join(secondary_diagonal_els)}. Sum: {secondary_diagonal}")

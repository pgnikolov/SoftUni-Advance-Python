rows = int(input())
matrix = [[int(num) for num in input().split()] for _ in range(rows)]

primary_sum = 0
secondary_sum = 0

for i in range(len(matrix)):
    primary_sum += matrix[i][i]
    secondary_sum += matrix[i][rows - i - 1]

print(abs(primary_sum - secondary_sum))

n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

sum_primary = 0
for i in range(len(matrix)):
    sum_primary += matrix[i][i]

print(sum_primary)

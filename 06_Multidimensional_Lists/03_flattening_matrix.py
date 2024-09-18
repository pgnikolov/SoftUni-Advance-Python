rows = int(input())

matrix = []

for _ in range(rows):
    row_elements = input().split(", ")
    matrix.extend(map(int, row_elements))

print(matrix)

rows = int(input())
matrix = [list(input()) for _ in range(rows)]
cols = len(matrix[0])

movement = [
    (-2, -1), (-2, 1), (2, -1), (2, 1),
    (-1, -2), (1, -2), (-1, 2), (1, 2)
]


def is_valid_index(row, col):
    return 0 <= row < rows and 0 <= col < cols


def count_attacks(row, col):
    attacks = 0
    for dr, dc in movement:
        nr, nc = row + dr, col + dc
        if is_valid_index(nr, nc) and matrix[nr][nc] == "K":
            attacks += 1
    return attacks


total_knights_removed = 0

while True:
    max_attacks = 0
    knight_to_remove = None

    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == "K":
                attacks = count_attacks(row, col)
                if attacks > max_attacks:
                    max_attacks = attacks
                    knight_to_remove = (row, col)

    if max_attacks == 0:
        break

    row, col = knight_to_remove
    matrix[row][col] = "0"
    total_knights_removed += 1

print(total_knights_removed)

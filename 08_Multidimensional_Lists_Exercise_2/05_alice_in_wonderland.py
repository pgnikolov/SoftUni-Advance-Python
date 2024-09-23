def read_matrix(rows):
    wonderland = []
    for _ in range(rows):
        row = input().split()
        wonderland.append(row)
    return wonderland


def find_alice(wonderland, rows):
    for r in range(rows):
        for c in range(rows):
            if matrix[r][c] == "A":
                return r, c


def moves(position, direction):
    row, col = position
    if direction == "up":
        return row - 1, col
    elif direction == "down":
        return row + 1, col
    elif direction == "left":
        return row, col - 1
    elif direction == "right":
        return row, col + 1


def within_wonderland(position, rows):
    row, col = position
    return 0 <= row < n and 0 <= col < rows


def alice_adventure(wonderland, rows):
    directions = {
        'up': (-1, 0),
        'down': (1, 0),
        'left': (0, -1),
        'right': (0, 1),
    }

    tea_bags_collected = 0
    alice_r, alice_c = find_alice(wonderland, rows)
    wonderland[alice_r][alice_c] = "*"

    while tea_bags_collected < 10:
        new_move = input().strip()
        move_r, move_c = directions[new_move]
        new_r, new_c = alice_r + move_r, alice_c + move_c

        if not within_wonderland((new_r, new_c), n):
            print("Alice didn't make it to the tea party.")
            break

        if wonderland[new_r][new_c] == "R":
            wonderland[new_r][new_c] = "*"
            print("Alice didn't make it to the tea party.")
            break

        if wonderland[new_r][new_c].isdigit():
            tea_bags_collected += int(wonderland[new_r][new_c])

        wonderland[new_r][new_c] = "*"
        alice_r, alice_c = new_r, new_c

        if tea_bags_collected >= 10:
            print("She did it! She went to the party.")
            break

    for row in wonderland:
        print(' '.join(row))


n = int(input())
matrix = read_matrix(n)

alice_adventure(matrix, n)

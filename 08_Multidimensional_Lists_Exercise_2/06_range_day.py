def read_matrix():
    return [[x for x in input().split()] for _ in range(5)]


def count_total_targets(matrix):
    return sum(matrix[row].count("x") for row in range(5))


def find_player(matrix):
    for row in range(5):
        if "A" in matrix[row]:
            col = matrix[row].index("A")
            matrix[row][col] = "."
            return row, col


def check_valid_index(row, col):
    return 0 <= row < 5 and 0 <= col < 5


def shoot(matrix, row, col, direction, directions, dead_targets_pos, total_targets):
    for _ in range(5):
        shooting_row, shooting_col = row + directions[direction][0], col + directions[direction][1]
        if check_valid_index(shooting_row, shooting_col):
            if matrix[shooting_row][shooting_col] == "x":
                total_targets[0] -= 1
                dead_targets_pos.append([shooting_row, shooting_col])
                matrix[shooting_row][shooting_col] = "."
                break
            row, col = shooting_row, shooting_col
        else:
            break


def move(matrix, row, col, direction, steps, directions):
    total_step = [x * steps if x != 0 else 0 for x in directions[direction]]
    moving_row, moving_col = row + total_step[0], col + total_step[1]
    if check_valid_index(moving_row, moving_col) and matrix[moving_row][moving_col] == ".":
        matrix[row][col] = "."
        matrix[moving_row][moving_col] = "A"
        return moving_row, moving_col
    return row, col


def show_result(dead_targets_pos):
    for pos in dead_targets_pos:
        print(pos)


matrix = read_matrix()
total_targets = [count_total_targets(matrix)]
dead_targets_pos = []
directions = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}
player_row, player_col = find_player(matrix)
number_of_commands = int(input())

for _ in range(number_of_commands):
    command = input().split()
    if command[0] == "shoot":
        shoot(matrix, player_row, player_col, command[1], directions, dead_targets_pos, total_targets)
    elif command[0] == "move":
        player_row, player_col = move(matrix, player_row, player_col, command[1], int(command[2]), directions)
    if total_targets[0] == 0:
        print(f"Training completed! All {len(dead_targets_pos)} targets hit.")
        show_result(dead_targets_pos)
        break
else:
    print(f"Training not completed! {total_targets[0]} targets left.")
    show_result(dead_targets_pos)

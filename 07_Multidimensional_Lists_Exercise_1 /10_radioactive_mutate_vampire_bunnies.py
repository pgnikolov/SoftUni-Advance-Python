rows, cols = map(int, input().split())
matrix = [[char for char in input()] for _ in range(rows)]
commands = [char for char in input()]

is_winner = False
movements = {"U": [-1, 0], "D": [1, 0], "L": [0, -1], "R": [0, 1]}


def locate_player():
    for row_idx in range(rows):
        if "P" in matrix[row_idx]:
            return row_idx, matrix[row_idx].index("P")


def check_player_status(row, col):
    if matrix[row][col] == "B":
        display_result("dead")


def valid_position(row, col, player_check=False):
    global is_winner
    if 0 <= row < rows and 0 <= col < cols:
        return True
    if player_check:
        is_winner = True


def get_bunnies_positions():
    bunnies = []
    for row_idx in range(rows):
        for col_idx in range(cols):
            if matrix[row_idx][col_idx] == "B":
                bunnies.extend((row_idx, col_idx))
    return bunnies


def move_bunnies(bunnies_pos):
    for i in range(0, len(bunnies_pos), 2):
        bunny_row, bunny_col = bunnies_pos[i], bunnies_pos[i + 1]
        for direction in movements.values():
            new_row, new_col = bunny_row + direction[0], bunny_col + direction[1]
            if valid_position(new_row, new_col):
                matrix[new_row][new_col] = "B"


def display_result(status="won"):
    for row in matrix:
        print("".join(row))
    print(f"{status}: {player_row} {player_col}")
    exit()


player_row, player_col = locate_player()
matrix[player_row][player_col] = "."
for command in commands:
    move_row, move_col = player_row + movements[command][0], player_col + movements[command][1]
    if valid_position(move_row, move_col, True):
        player_row, player_col = move_row, move_col
    move_bunnies(get_bunnies_positions())
    if is_winner:
        display_result()
    if valid_position(move_row, move_col):
        check_player_status(move_row, move_col)

rows, cols = map(int, input().split())

matrix = [[char for char in input().split()] for _ in range(rows)]

while True:
    command = input().split()
    if command[0] == 'END':
        break
    elif command[0] == 'swap':
        if len(command) == 5:
            row1, col1, row2, col2 = int(command[1]), int(command[2]), int(command[3]), int(command[4])
            if 0 <= row1 < rows and 0 <= row2 < rows and 0 <= col1 < cols and 0 <= col2 < cols:
                matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
                for row in matrix:
                    print(" ".join(map(str, row)))
            else:
                print('Invalid input!')
                continue
        else:
            print('Invalid input!')
            continue
    else:
        print('Invalid input!')
        continue

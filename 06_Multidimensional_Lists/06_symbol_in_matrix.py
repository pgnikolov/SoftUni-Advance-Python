n = int(input())
matrix = [[char for char in input()] for _ in range(n)]
wanted_symbol = input()

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == wanted_symbol:
            print(f'({i}, {j})')
            quit()
else:
    print(f'{wanted_symbol} does not occur in the matrix')
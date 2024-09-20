row, cols = map(int, input().split())
matrix = []
start_letter = 'a'

for i in range(row):
    matrix.append([])
    for j in range(cols):
        word = chr(ord(start_letter) + i) + chr(ord(start_letter) + i + j) + chr(ord(start_letter) + i)
        matrix[i].append(word)

for row in matrix:
    print(" ".join(row))

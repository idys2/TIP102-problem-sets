'''
- input: 2D integer array
- output: transposed 2D integer array
- 
- cases:
- normal case: element at [x][y] -> [y][x]
- 1. empty matrix: return empty matrix
'''

def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    if rows == 0 or cols == 0:
        return [[]]

    result = [[0] * rows for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]

    return result

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(transpose(matrix))

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(transpose(matrix))

matrix = [[]]
print(transpose(matrix))

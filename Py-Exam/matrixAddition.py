#19. **Matrix Addition (2D List)**
#    Take two 2×2 matrices and perform matrix addition.
matrix1 = [
    [1,2],
    [3,4]
]
matrix2 = [
    [5,6],
    [7,8]
]

result = [
    [0,0],
    [0,0]
]

for i in range(2):
    for j in range(2):
        result[i][j] = matrix1[i][j] + matrix2[i][j]
        
print("Matrix 1:", matrix1)
print("Matrix 2:", matrix2)
print("Result: ", result)
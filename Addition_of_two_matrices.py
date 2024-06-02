# Addition of two matrices
matA = [[1,2,3],
        [4,5,6],
        [7,8,9]]
matB = [[23,45,76],
        [21,34,65],
        [67,53,24]]
result = [[0,0,0],
         [0,0,0],
         [0,0,0]]
for i in range(len(matA)):
    for j in range(len(matA[0])):
        result[i][j] = matA[i][j]+matB[i][j]
for r in result:
    print(r)
    
def matrix_multiplication(X, Y, result):
    for i in range(len(X)):
       for j in range(len(Y[0])):
           for k in range(len(Y)):
               result[i][j] += X[i][k] * Y[k][j]
    for r in result:
       print(r)

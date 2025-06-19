# Two Dimensional Arrays # (Matrices) Operations 

def Matrix_Addition(A, B):
    n = len(A)
    C = [[0 for j in range(len(A[0]))] for i in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] + B[i][j]
    return C

def Matrix_Multiplication(A, B):
    n = len(A)
    C = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

A = [[1, 2], [3, 4]]
B = [[2, 4], [3, 1]]
C = Matrix_Addition(A, B)
print("A + B =", C)

C = Matrix_Multiplication(A, B)
print("A * B =", C)

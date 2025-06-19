#
# One-Dimensinal Array (Vector) Operations
#

A = [1, 2, 3, 4]
B = [2, 4, 3, 1]

C = [0 for i in range(len(A))]
# Addition

for i in range(len(A)):
    C[i] = A[i] + B[i]
print("A + B =", C)

# Multiplication
scalar = 3
for i in range(len(A)):
    C[i] = scalar * A[i]
print("3 * A =", C)

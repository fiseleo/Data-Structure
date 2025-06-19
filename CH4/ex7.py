def magic_square(n):
    A = [[0] * n for _ in range(n)]
    num = 1
    i, j = 0, n // 2  # Start in the middle of the first row
    while num <= n * n:
        A[i][j] = num
        num += 1
        new_i, new_j = (i - 1) % n, (j + 1) % n  # Move up and right
        if A[new_i][new_j] != 0:  # If the cell is already filled
            i += 1  # Move down instead
        else:
            i, j = new_i, new_j  # Update to the new position
    return A

def print_magic_square(square):
    n = len(square)
    for i in range(n):
        for j in range(n):
            print(f"{square[i][j]:3d}", end=" ")
        print()
    
while True:
    n = eval(input("Enter the size of the magic square (odd number): "))
    if n % 2 == 1:
        break
    else:
        print("Please enter an odd number.")

square = magic_square(n)
print_magic_square(square)
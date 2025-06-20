# Solve  simultaneous equations

import numpy as np
def solve_simultaneous_equations():
    # Coefficients for x, y, z

    A = np.array([[1,1,1], [2,3,4], [3,2,-1]]) 
    D = np.array([9, 29, 8])
    # Solve the system of equations
    solution = np.linalg.solve(A, D)
    return solution

print("Solution to the simultaneous equations:")
solution = solve_simultaneous_equations()
print(f"x = {solution[0]}, y = {solution[1]}, z = {solution[2]}")

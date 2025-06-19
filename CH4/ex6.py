import numpy as np

def chichens_and_rabbits(H,L):
    A = np.array([[1, 1], [2, 4]])
    b = np.array([H, L])
    A_inv = np.linalg.inv(A)
    solution = np.dot(A_inv, b)
    chickens = int(solution[0])
    rabbits = int(solution[1])
    if (chickens > 0 and rabbits > 0) and \
        chickens + rabbits == H and \
        2 * chickens + 4 * rabbits == L:
            return True, chickens, rabbits
    else:
        return False, None, None
    

print("Chickens and Rabbits Problem")
H = eval(input("Enter the total number of chickens and rabbits: "))
L = eval(input("Enter the total number of legs: "))
ok, chickens, rabbits = chichens_and_rabbits(H, L)
if ok:
    print(f"Chickens: {chickens}, Rabbits: {rabbits}")
else:
    print("No valid solution found.")

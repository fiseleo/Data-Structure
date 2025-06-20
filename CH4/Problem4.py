# Polynomial 
# Two Dimensional Polynomial Class
import collections.abc

class Polynomial2D:
    def __init__(self, coeffs):
        if not isinstance(coeffs, list) or not all(isinstance(row, collections.abc.Sequence) for row in coeffs):
            raise ValueError("Coefficients must be a list of lists.")
        self.coeffs = [list(row) for row in coeffs]
        self._trim()

    def _trim(self):
        for i in range(len(self.coeffs)):
            row = self.coeffs[i]
            while len(row) > 1 and row[-1] == 0:
                row.pop()
        while len(self.coeffs) > 1 and self.coeffs[-1] in ([0], []):
            self.coeffs.pop()
        if not self.coeffs:
            self.coeffs = [[0]]
        
    
    def Evaluate(self, x, y):
        y_result = 0
        for j in range(len(self.coeffs) -1, -1 , -1):
            x_result = 0
            row = self.coeffs[j]
            for i in range(len(row) - 1, -1, -1):
                x_result = x_result * x + row[i]
            y_result = y_result * y + x_result
        return y_result    
    
    def __add__(self, other):
        p1 = self.coeffs
        p2 = other.coeffs
        num_rows= max(len(p1), len(p2))
        num_cols = max(max(len(r) for r in p1), max(len(r) for r in p2) if p1 and p2 else 0)
        result_coeffs = [[0] * num_cols for _ in range(num_rows)]
        for j, row in enumerate(p1):
            for i, coeff in enumerate(row):
                result_coeffs[j][i] += coeff
        for j, row in enumerate(p2):
            for i, coeff in enumerate(row):
                result_coeffs[j][i] += coeff
        return Polynomial2D(result_coeffs)
    
    def __mul__(self, other):
        p1 = self.coeffs
        p2 = other.coeffs
        deg1_y, deg1_x = len(p1) - 1, max(len(r) for r in p1) - 1
        deg2_y, deg2_x = len(p2) - 1, max(len(r) for r in p2) - 1
        new_deg_y = deg1_y + deg2_y
        new_deg_x = deg1_x + deg2_x

        result_coeffs = [[0] * (new_deg_x + 1) for _ in range(new_deg_y + 1)]

        for j1, row1 in enumerate(p1):
            for i1, coeff1 in enumerate(row1):
                if coeff1 == 0: continue
                for j2, row2 in enumerate(p2):
                    for i2, coeff2 in enumerate(row2):
                        if coeff2 == 0: continue
                        result_coeffs[j1 + j2][i1 + i2] += coeff1 * coeff2
        return Polynomial2D(result_coeffs)
    
    def Display(self):
        terms = []
        for j in range(len(self.coeffs) - 1, -1, -1):
            row = self.coeffs[j]
            for i in range(len(row) - 1, -1, -1):
                coeff = row[i]
                if coeff == 0:
                    continue
                term = ""
                if len(terms) > 0 :
                    term += " + " if coeff > 0 else " - "
                    coeff = abs(coeff)
                elif coeff < 0:
                    term += "-"
                    coeff = abs(coeff)
                if i == 0 and j == 0:
                    term += f"{coeff}"
                elif coeff != 1 or (i == 0 and j == 0):
                    term += f"{coeff}"
                if i > 0:
                    term += "x"
                    if i > 1:
                        term += f"^{i}"
                if j > 0:
                    term += "y"
                    if j > 1:
                        term += f"^{j}"
                terms.append(term)
        return "".join(terms) if terms else "0"
# P1(x, y) = 2x + 3y + 1
# 係數表示:
# y^0: 1*x^0 + 2*x^1  -> [1, 2]
# y^1: 3*x^0          -> [3]
p1_coeffs = [[1, 2], [3]]
p = Polynomial2D(p1_coeffs)

x, y = 1, 2
print(f"Polynomial 1: {p.Display()}")
print(f"P1({x}, {y}) = {p.Evaluate(x, y)}")

# P2(x, y) = 2x + xy + y +5
# 係數表示:
# y^0: 5*x^0 + 2*x^1 + 1*x^1 -> [5, 2, 1]
# y^1: 1*x^0 -> [1]

p2_coeffs = [[5,2], [1,1]]
p2 = Polynomial2D(p2_coeffs)
print(f"Polynomial 2: {p2.Display()}")
x, y = 1, 1
print(f"P2({x}, {y}) = {p2.Evaluate(x, y)}")

p3 = p + p2
print(f"P1 + P2: {p3.Display()}")
p4 = p * p2
print(f"P1 * P2: {p4.Display()}")

# 係數陣列 coeffs 是一個二維列表，其中 coeffs[j][i] 儲存的是 x^i * y^j 的係數。
# 例如，coeffs[0][1] 儲存的是 x^1 * y^0 的係數，coeffs[1][0] 儲存的是 x^0 * y^1 的係數。

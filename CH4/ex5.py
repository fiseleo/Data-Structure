class Polynomial:
    def __init__(self, coeffs):
        self.coeffs = coeffs

    def Evaluate(self, x):
        result = 0
        for coeff in self.coeffs:
            result = result * x + coeff # Horner's method
        return result

    def __add__(self, other):
        p1 = self.coeffs
        p2 = other.coeffs
        if len(p1) < len(p2):
            p1 = [0] * (len(p2) - len(p1)) + p1
        elif len(p2) < len(p1):
            p2 = [0] * (len(p1) - len(p2)) + p2
        result_coeffs = [0] * len(p1)
        for i in range(len(p1)):
            result_coeffs[i] = p1[i] + p2[i]
        return Polynomial(result_coeffs)
    
    def __mul__(self, other):
        p1 = self.coeffs
        p2 = other.coeffs
        n = len(p1) + len(p2) - 1
        result_coeffs = [0] * n
        for i in range(len(p1)):
            for j in range(len(p2)):
                result_coeffs[i + j] += p1[i] * p2[j]
        return Polynomial(result_coeffs)
    
    def Display(self):
        terms= []
        degee = len(self.coeffs) - 1
        for i in range(len(self.coeffs)):
            coeff = self.coeffs[i]
            if coeff != 0:
                if degee - i == 0:
                    terms.append(f"{coeff}")
                elif degee - i == 1:
                    if coeff == 1:
                        terms.append("x")
                    elif coeff == -1:
                        terms.append("-x")
                    else:
                        terms.append(f"{coeff}x")
                else:
                    if coeff == 1:
                        terms.append(f"x^{degee - i}")
                    elif coeff == -1:
                        terms.append(f"-x^{degee - i}")
                    else:
                        terms.append(f"{coeff}x^{degee - i}")
        return " + ".join(terms).replace(" + -", " - ")
    
p = Polynomial([1, -2, 1])  # Represents x^2 - 2x + 1
x = 3
print(f"Polynomial: {p.Display()}")
print(f"Value at x={x}: {p.Evaluate(x)}")

p1 = Polynomial([1, 0, -1])  # Represents x^2 - 1
p2 = Polynomial([1, 2])      # Represents 2x + 1
print(f"Sum: {p1.Display()} + {p2.Display()} = {(p1 + p2).Display()}")

p1 = Polynomial([1, 0, -1])  # Represents x^2 - 1
p2 = Polynomial([1, 2])      # Represents 2x + 1
p = p1 * p2
print(f"Product: {p1.Display()} * {p2.Display()} = {p.Display()}")
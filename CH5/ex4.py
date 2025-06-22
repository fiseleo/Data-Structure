# Using Linked List  Polynomial

class Node:
    def __init__(self, coeff, exponent):
        self.coeff = coeff
        self.exponent = exponent
        self.next = None

class Polynomial:
    def __init__(self):
        self.head = None
    

    def Insert(self, coeff, exponent):
        new_term = Node(coeff, exponent)
        if self.head is None:
            self.head = new_term
        else:
            current = self.head
            while  current.next:
                current = current.next
            current.next = new_term

    
    def Evaluate(self, x):
        result = 0
        current = self.head
        while current:
            result += current.coeff * (x ** current.exponent)
            current = current.next
        return result
    
    def __add__(self, other_poly):
        result = Polynomial()
        current1 = self.head
        current2 = other_poly.head
        while current1 and current2:
            if current1.exponent > current2.exponent:
                result.Insert(current1.coeff, current1.exponent)
                current1 = current1.next
            elif current1.exponent < current2.exponent:
                result.Insert(current2.coeff, current2.exponent)
                current2 = current2.next
            else:
                new_coeff = current1.coeff + current2.coeff
                result.Insert(new_coeff, current1.exponent)
                current1 = current1.next
                current2 = current2.next
        while current1:
            result.Insert(current1.coeff, current1.exponent)
            current1 = current1.next
        while current2:
            result.Insert(current2.coeff, current2.exponent)
            current2 = current2.next
        return result
    
    def __mul__(self, other_poly):
        result = Polynomial()
        current1 = self.head
        while current1:
            current2 = other_poly.head
            while current2:
                new_coeff = current1.coeff * current2.coeff
                new_exp = current1.exponent + current2.exponent
                temp = result.head
                prev = None
                while temp and temp.exponent > new_exp:
                    prev = temp
                    temp = temp.next
                if temp and temp.exponent == new_exp:
                    temp.coeff += new_coeff
                else:
                    new_term = Node(new_coeff, new_exp)
                    if prev is None:
                        new_term.next = result.head
                        result.head = new_term
                    else:
                        new_term.next = temp
                        prev.next = new_term
                current2 = current2.next
            current1 = current1.next
        return result
    

    def Display(self):
        current = self.head
        polynomial_str = ""
        firest_term = True
        while current:
            if current.coeff != 0:
                if current.coeff > 0 and not firest_term:
                    polynomial_str += " + "
                elif current.coeff < 0:
                    polynomial_str += " - "
                if abs(current.coeff) != 1 or current.exponent == 0:
                    polynomial_str += str(abs(current.coeff))
                if current.exponent > 0:
                    polynomial_str += f"x"
                    if current.exponent > 1:
                        polynomial_str += f"^{current.exponent}"
                firest_term = False
            current = current.next
        if polynomial_str.startswith(" + "):
            polynomial_str = polynomial_str[1:]

        print(polynomial_str)



# Example usage
p = Polynomial()
p.Insert(1, 3) # 1x^3
p.Insert(2, 2) # 2x^2
p.Insert(3, 1) # 3x^1
p.Insert(5, 0) # 5x^0

value = p.Evaluate(2)
print(f"Polynomial evaluated at x=2: {value}")
p.Display()

print("多項式的函數值 =", value)

p1 = Polynomial()
p1.Insert(1, 3)
p1.Insert(2, 2)
p1.Insert(3, 1)
p1.Insert(5, 0)
p2 = Polynomial()
p2.Insert(2, 4)
p2.Insert(1, 3)
p2.Insert(4, 2)
p2.Insert(1, 1)
p2.Insert(3, 0)

print("p1(x) =", end=" ")
p1.Display()
print("p2(x) =", end=" ")
p2.Display()

p3 = p1 + p2
print("p1 + p2 =", end=" ")
p3.Display()

p4 = p1 * p2
print("p1 * p2 =", end=" ")
p4.Display()


            


        

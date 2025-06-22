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
            while current = current.next:
                current = current.next
            current.next = new_term

    
    def Evaluate(self, x):
        

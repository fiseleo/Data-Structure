# infix to postfix

class Stack:
    def __init__(self):
        self.S = []

    def isEmpty(self):
        return self.S == []
    
    def Push(self, key):
        self.S.append(key)
    
    def Pop(self):
        if self.isEmpty():
            print("Stack is empty")
            return None
        else:
            return self.S.pop()
    
    def Peek(self):
        if self.isEmpty():
            print("Stack is empty")
            return None
        else:
            return self.S[-1]
        
    def Display(self):
        print("Stack elements are: ", end="")
        print(self.S)


def handle_operator(op, operators, output, precedence):
    while (not operators.isEmpty() and operators.Peek() != '(' and\
            precedence.get(operators.Peek(), 0) >= precedence[op]):
        output.append(operators.Pop())
    operators.Push(op)

def infix_to_postfix(expression):
    precedence = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '^': 3
    }

    output = []
    operators = Stack()
    tokens = expression.split()
    for token in tokens:
        if token.isalnum():
            output.append(token)
        elif token in precedence:
            handle_operator(token, operators, output, precedence)
        elif token == '(':
            operators.Push(token)
        elif token == ')':
            while not operators.isEmpty() and operators.Peek() != '(':
                output.append(operators.Pop())
            operators.Pop()
    while not operators.isEmpty():
        output.append(operators.Pop())

    
    return ' '.join(output)

def evaluate_postfix(expression, values):
    stack = Stack()
    tokens = expression.split()
    for token in tokens:
        if token.isalnum():
            stack.Push(values[token])
        else:
            operand2 = stack.Pop()
            operand1 = stack.Pop()
            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            elif token == '/':
                if operand2 == 0:
                    print("Error: Division by zero")
                    return None
                result = operand1 / operand2
            elif token == '^':
                result = operand1 ** operand2
            stack.Push(result)
    return stack.Pop()

# Example usage
print("Infix to Postfix Conversion")
infix_expression = "( A  + B ) * C + D / E"
postfix_expression = infix_to_postfix(infix_expression)
print(f"Infix: {infix_expression}")
print(f"Postfix: {postfix_expression}")

print("\nPostfix Evaluation")
values = {
    'A': 1,
    'B': 3,
    'C': 4,
    'D': 10,
    'E': 2
}
postfix_result = evaluate_postfix(postfix_expression, values)
print(f"Postfix Expression: {postfix_expression}")
print(f"Evaluation Result: {postfix_result}")
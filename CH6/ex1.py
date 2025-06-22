# Stack

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
        if self.isEmpty():
            print("Stack is empty")
        else:
            print("Stack elements are: ", end="")
            print(self.S)
    

# Example usage
S = Stack()
S.Push(10)
S.Push(20)
S.Push(30)
S.Display()
# Last In First Out (LIFO) principle
S.Pop() # Removes 30
# Peek 是查看堆疊（Stack）最頂端的元素，但不會將其移除。
A = S.Peek() # Returns 20
print(f"Top element is: {A}")
S.Display()
# Palindrome

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
    
    def Display(self):
        print("Stack elements are: ", end="")
        print(self.S)

def isPalindrome(s):
        stack = Stack()
        for char in s:
            stack.Push(char)
        for char in s:
            if char != stack.Pop():
                return False
        return True
    

s = "radar"
if isPalindrome(s):
    print(f"{s} is a palindrome")
else:
    print(f"{s} is not a palindrome")

s = "madam"
if isPalindrome(s):
    print(f"{s} is a palindrome")
else:
    print(f"{s} is not a palindrome")
s = "hello"
if isPalindrome(s):
    print(f"{s} is a palindrome")
else:
    print(f"{s} is not a palindrome")
s = "上海自来水来自海上"
if isPalindrome(s):
    print(f"{s} is a palindrome")
else:
    print(f"{s} is not a palindrome")
s = "天天都是好日子"
if isPalindrome(s):
    print(f"{s} is a palindrome")
else:
    print(f"{s} is not a palindrome")



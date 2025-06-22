class Queue:
    def __init__(self):
        self.Q = []
    
    def isEmpty(self):
        return self.Q == []
    
    def Enqueue(self, key):
        self.Q.append(key)
    
    def Dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
            return None
        else:
            return self.Q.pop(0)
    
    def Display(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            print("Queue elements are: ", end="")
            print(self.Q)
    

# Example usage
Q = Queue()
Q.Enqueue(10) # 最早加入的元素
Q.Enqueue(20)
Q.Enqueue(30)
Q.Display()
# First In First Out (FIFO) principle
Q.Dequeue()  # Removes 10
Q.Display()
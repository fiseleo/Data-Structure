# Circular Queue

class CircularQueue:
    def __init__(self ,size):
        self.Q = [None] * size
        self.size = size
        self.front = -1
        self.rear = -1

    
    # 看是否empty

    def isEmpty(self):
        return self.front == -1
    
    # 看有沒有full
    def isFull(self):
        return (self.rear + 1) % self.size == self.front
    
    def Enqueue(self, key):
        if self.isFull():
            print("Queue is full")
            return
        if self.isEmpty():
            self.front = 0
        
        self.rear = (self.rear + 1) % self.size

        self.Q[self.rear] = key


    def Dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
            return None
        result = self.Q[self.front]
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return result
    
    # 來將 front 指標移動到下一個元素。
    # 當 self.front 已經在陣列的最後一個位置（即 self.size - 1）時，self.front + 1 就會等於 self.size。
    # 此時 self.size % self.size 的結果是 0。 這就巧妙地讓指標「繞回」到了陣列的起始位置 0，形成了環狀。
    # %  (模數運算子 - Modulo Operator)
    
    def Display(self):
        print("Queue elements are: ", end="")
        if self.rear >= self.front:
            print(self.Q[self.front:self.rear + 1])
        else:
            print(self.Q[self.front:] + self.Q[:self.rear + 1])


# Example usage
Q = CircularQueue(8)
Q.Enqueue(10)  # 最早加入的元素
Q.Enqueue(20)
Q.Enqueue(30)
Q.Enqueue(40)
Q.Enqueue(50)
Q.Display()
Q.Dequeue()  # Removes 10
Q.Display()
# Circular Linked List

class Node:
    def __init__(self, key=None):
        self.key = key
        self.next = None
        self.prev = None

class CircularLinkedList:
    def __init__(self):
        self.head = Node()
        self.head.prev= self.head
        self.head.next = self.head
    
    def Search(self, key):
        current = self.head
        while current != self.head:
            if current.key == key:
                return True
            current = current.next
        return False

    def Insert(self, key):
        newNode = Node(key)
        newNode.next = self.head.next
        newNode.prev = self.head
        self.head.next.prev = newNode
        self.head.next = newNode


    def InsertTail(self, key):
        newNode = Node(key)
        newNode.prev = self.head.prev
        newNode.next = self.head
        self.head.prev.next = newNode
        self.head.prev = newNode

    def Delete(self):
        if self.head is None:
            print("List is empty")
        else:
            current = self.head.next
            self.head.next = current.next
            current.next.prev = self.head
    
    def DeleteTail(self):
        if self.head.next == self.head:
            print("List is empty")
        else:
            current = self.head.prev
            current.prev.next = self.head
            self.head.prev = current.prev

        
    def Display(self):
        if self.head.next == self.head:
            print("List is empty")
        else:
            print("Circular Linked List: ", end="")
            current = self.head.next
            while current != self.head:
                print(current.key, end=" ")
                current = current.next
            print()



## Example usage
cll = CircularLinkedList()
cll.Insert(10)
cll.Insert(20)
cll.Insert(30)
cll.Display()  # Output: Circular Linked List: 30 20 10
cll.InsertTail(40)
cll.Display()  # Output: Circular Linked List: 30 20 10 40
cll.Delete()
cll.Display()  # Output: Circular Linked List: 20 10 40
cll.DeleteTail()
cll.Display()  # Output: Circular Linked List: 20 10


            
        

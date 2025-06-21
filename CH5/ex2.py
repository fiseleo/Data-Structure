# Doubly Linked List

class Node:
    def __init__(self, key=None):
        self.key = key
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, head=None):
        self.head = None


    def Search(self, key):
        current = self.head
        while current:
            if current.key == key:
                return True
            current = current.next
        return False
    
    def Insert(self, key):
        newNode = Node(key)
        if not self.head:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
    
    def InsertTail(self, key):
        newNode = Node(key)
        if not self.head:
            self.head = newNode
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
            newNode.prev = current

    def Delete(self):
        if self.head is None:
            print("List is empty")
        else:
            if self.head.next is None:
                self.head = None
            else:
                self.head = self.head.next
                self.head.prev = None
    
    def DeleteTail(self):
        if self.head is None:
            print("List is empty")
        else:
            if self.head.next is None:
                self.head = None
            else:
                current = self.head
                while current.next:
                    current = current.next
                current.prev.next = None

    def Display(self):
        if self.head is None:
            print("List is empty")
        else:
            print("List elements are: ", end="")
            current = self.head
            while current:
                print(current.key, end=" ")
                current = current.next
            print()


# Example usage
dll = DoublyLinkedList()
dll.Insert(10)
dll.Insert(20)
dll.Insert(30)
dll.Display()  # Output: List elements are: 30 20 10
dll.InsertTail(40)
dll.Display()  # Output: List elements are: 30 20 10 40
dll.Delete()
dll.Display()  # Output: List elements are: 20 10 40
dll.DeleteTail()
dll.Display()  # Output: List elements are: 20 10




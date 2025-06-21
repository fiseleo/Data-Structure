# Singly Linked List example

class Node:
    def __init__(self , key = None):

        self.key = key
        self.next = None


class SinglyLinkedList:
    def __init__(self, head=None):
        self.head = None

    
    def Seach(self, key):
        current = self.head
        while current:
            if current.key == key:
                return True
            
            current = current.next
        return False
    
    def Insert(self , key):
        newNode = Node(key)
        newNode.next = self.head
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
    def Delete(self):
        if self.head is None:
            print("List is empty")
        else:
            self.head = self.head.next

    def DeleteTail(self):
        if self.head is None:
            print("List is empty")
        else:
            if self.head.next is None:
                self.head = None
            else:
                current = self.head
                while current.next and current.next.next:
                    current = current.next
                current.next = None

    def Display(self):
        if self.head is None:
            print("List is empty")
        else:
            print("List elements are: ", end="")
            current = self.head
            while current:
                print(current.key, end=" -> ")
                current = current.next
            print("None")



# Example usage
sll = SinglyLinkedList()
sll.Insert(10)
sll.Insert(20)
sll.Insert(30)
sll.InsertTail(40)
sll.Display()  # Output: List elements are: 30 -> 20 -> 10 -> 40 -> None
sll.Delete() 
sll.Display()  # Output: List elements are: 20 -> 10 -> 40 -> None
sll.DeleteTail()
sll.Display()  # Output: List elements are: 2   0 -> 10 -> None


        



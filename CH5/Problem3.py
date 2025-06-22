# Singly Linked List
#  key  > 張小明,男,19,台北市

class Node:
    def __init__(self, key=None):
        self.key = key
        self.next = None

class SinglyLinkedList:
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


# Example usage:
sll = SinglyLinkedList()
sll.Insert("張小明,男,19,台北市")
sll.Insert("王小花,女,18,桃園市")
sll.Insert("李大發,男,22,台中市")
sll.Insert("陳小東,男,13,高雄市")

sll.Display()
sll.Delete()
sll.Display()
sll.InsertTail("林小美,女,20,新竹市")
sll.Display()
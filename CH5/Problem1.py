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

    def Length(self):
        conut = 0
        current = self.head
        while current:
            conut += 1
            current = current.next
        return conut
    
    def Sum(self):
        total = 0
        current = self.head
        while current:
            total += current.key
            current = current.next
        return total
    
    def InsertSort(self, key):
        newNode = Node(key)
        # Insert the new node in sorted order
        # 當前的頭節點為空或新節點的鍵小於等於頭節點的鍵時，將新節點插入到頭部
        if not self.head or self.head.key >= key:
            newNode.next = self.head
            self.head = newNode
        else:
            current = self.head
            # 當前節點的下一個節點存在且下一個節點的鍵小於新節點的鍵時，繼續向後遍歷
            # 找到適當的位置插入新節點
            while current.next and current.next.key < key:
                current = current.next
            newNode.next = current.next
            current.next = newNode
    
    def Reverse(self):
        prev = None
        current = self.head
        # 反轉鏈表
        # 當前節點存在時，將當前節點的下一個節點指向前一個節點
        # 並將前一個節點更新為當前節點，當前節點更新為下一個節點
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev


# Example usage:
sll = SinglyLinkedList()
sll.Insert(3)
sll.Insert(1)
sll.Insert(2)
A = sll.Length()  # Output: 3
print (f"Length of the list: {A}")
B = sll.Sum()     # Output: 6
print(f"Sum of the list elements: {B}")

sll.Delete()
sll.Delete()
sll.Delete()

sll.InsertSort(5)
sll.InsertSort(3)
sll.InsertSort(4)
sll.Display()  # Output: List elements are: 3 -> 4 -> 5 -> None
sll.Reverse()
sll.Display()  # Output: List elements are: 5 -> 4 -> 3 -> None




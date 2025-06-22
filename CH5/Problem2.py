# Bucket Sort
import random
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
    
    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.key)
            current = current.next
        return result
    
    def sort(self):
        lst = self.to_list()
        lst.sort()
        self.head = None
        for item in lst:
            self.InsertTail(item)

def bucket_sort(A):
    n = len(A)
    num_buckets = n
    buckets = [SinglyLinkedList() for _ in range(num_buckets)]

    for num in A:
        bucket_index = int(num * n)
        buckets[bucket_index].Insert(num)
    sorted_array = []
    for bucket in buckets:
        bucket.sort()
        sorted_array.extend(bucket.to_list())
    
    return sorted_array


# Example usage
# 生出100个随机数并进行桶排序
A = [ random.uniform(0, 1) for i in range(100) ]  # Generate 100 random numbers between 0 and 1
print("Original Array:", A) 
sorted_A = bucket_sort(A)
print("Sorted Array:", sorted_A)
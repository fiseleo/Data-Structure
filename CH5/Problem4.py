# Sparse Matrix  Using Linked List
#Examlpe 
# 1 0 0 0 0
# 0 0 0 0 2
# 0 3 0 0 0
# 0 0 0 4 0
# 0 0 0 0 5

class Node:
    def __init__(self, row, col, value):
        self.row = row
        self.col = col
        self.value = value
        self.next = None
class SparseMatrix:
    def __init__(self , row, col):
        self.head = None
        self.rows = row
        self.cols = col

    # Matrix 的插入
    def insert(self, row, col, value):
        if value == 0:
            return  # 不插入值為0的元素
        
        new_node = Node(row, col, value)

        # --- Case 1: 鏈結串列是空的，或新節點應該成為新的頭節點 ---
        if self.head is None or self.head.row > row or (self.head.row == row and self.head.col > col):
            new_node.next = self.head
            self.head = new_node
            return

        # --- Case 2: 要更新的節點正好是頭節點 ---
        if self.head.row == row and self.head.col == col:
            self.head.value += value
            # (優化) 如果更新後值變為 0，則移除頭節點
            if self.head.value == 0:
                self.head = self.head.next
            return

        # --- Case 3: 遍歷鏈結串列尋找插入點或更新點 ---
        current = self.head
        # 尋找插入點的前一個位置
        while current.next and (current.next.row < row or (current.next.row == row and current.next.col < col)):
            current = current.next
        
        # 在迴圈結束後，current 是目標位置的前一個節點。
        # 我們需要檢查 current.next 是否存在且位置是否相符。
        
        # --- Case 3a: 找到要更新的節點 (current.next) ---
        if current.next and current.next.row == row and current.next.col == col:
            current.next.value += value
            # (優化) 如果更新後值變為 0，則移除該節點
            if current.next.value == 0:
                current.next = current.next.next
        # --- Case 3b: 未找到對應節點，在此處插入新節點 ---
        else:
            new_node.next = current.next
            current.next = new_node
    # Matrix 的加法
    def add(self, other):
        """
        將此矩陣與另一個稀疏矩陣 'other' 相加，並返回一個新的結果矩陣。
        """
        if not isinstance(other, SparseMatrix):
            raise TypeError("只能與另一個 SparseMatrix 物件相加")

        result = SparseMatrix(self.rows, self.cols)
        
        current_self = self.head
        current_other = other.head

        # 當兩個矩陣都還有非零元素時
        while current_self and current_other:
            # 情況 1: self 的元素位置在 other 之前，直接插入 self 的元素
            if current_self.row < current_other.row or \
               (current_self.row == current_other.row and current_self.col < current_other.col):
                result.insert(current_self.row, current_self.col, current_self.value)
                current_self = current_self.next
            # 情況 2: other 的元素位置在 self 之前，直接插入 other 的元素
            elif current_self.row > current_other.row or \
                 (current_self.row == current_other.row and current_self.col > current_other.col):
                result.insert(current_other.row, current_other.col, current_other.value)
                current_other = current_other.next
            # 情況 3: 兩個元素位置相同，將值相加
            else:
                new_value = current_self.value + current_other.value
                if new_value != 0:
                    result.insert(current_self.row, current_self.col, new_value)
                current_self = current_self.next
                current_other = current_other.next
        
        # 將剩下還沒處理完的節點加入結果中
        # 如果 self 還有剩餘元素
        while current_self:
            result.insert(current_self.row, current_self.col, current_self.value)
            current_self = current_self.next
            
        # 如果 other 還有剩餘元素
        while current_other:
            result.insert(current_other.row, current_other.col, current_other.value)
            current_other = current_other.next
            
        return result
    # Matrix 的減法
    def delete(self, row, col):
        if self.head is None:
            print("Matrix is empty")
            return
        if self.head.row == row and self.head.col == col:
            self.head = self.head.next
            return
        current = self.head
        while current.next and (current.next.row < row or (current.next.row == row and current.next.col < col)):
            current = current.next
        if current.next and current.next.row == row and current.next.col == col:
            current.next = current.next.next
        else:
            print("Element not found in the matrix")
    # Matrix 的乘法
    def multiply(self, other):
        # 將此矩陣與另一個稀疏矩陣 'other' 相乘，並返回一個新的結果矩陣。
        # 當兩個矩陣 A (維度 m x n) 和 B (維度 n x p) 相乘時，結果矩陣 C 的維度會是 m x p。
        result = SparseMatrix(self.rows, other.cols)
        # 檢查矩陣維度是否匹配
        if self.cols != other.rows:
            raise ValueError("Matrix dimensions do not match for multiplication")
        current1 = self.head
        while current1:
            current2 = other.head
            while current2:
                if current1.col == current2.row:
                    value = current1.value * current2.value
                    if value != 0:
                        result.insert(current1.row, current2.col, value)
                current2 = current2.next
            current1 = current1.next
        return result
    
    def Display(self):
        if self.head is None:
            print("Matrix is empty")
        else:
            current = self.head
            while current:
                print(f"Row: {current.row}, Col: {current.col}, Value: {current.value}")
                current = current.next

    def print_as_matrix(self):
        grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        current = self.head
        while current:
            if 0 <= current.row < self.rows and 0 <= current.col < self.cols:
                grid[current.row][current.col] = current.value
            current = current.next
        
        for row in grid:
            print(" ".join(map(str, row)))

# Example usage
matrix_a = SparseMatrix(5, 5)
matrix_a.insert(0, 0, 1)
matrix_a.insert(1, 4, 2)
matrix_a.insert(2, 1, 3)
matrix_a.insert(3, 3, 4)
matrix_a.insert(4, 4, 5)
print("Matrix A:")
matrix_a.print_as_matrix()
matrix_a.Display()

matrix_b = SparseMatrix(5, 5)
matrix_b.insert(0, 1, 2)
matrix_b.insert(1, 2, 3)
matrix_b.insert(2, 3, 4)
matrix_b.insert(3, 4, 5)
print("Matrix B:")
matrix_b.print_as_matrix()

result_add = matrix_a.add(matrix_b)
print("Result of Addition: ")
result_add.print_as_matrix()
result_multiply = matrix_a.multiply(matrix_b)
print("Result of Multiplication: ")
result_multiply.print_as_matrix()



# Maze Problem

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
    
    def Peek(self):
        if self.isEmpty():
            print("Stack is empty")
            return None
        else:
            return self.S[-1]
        
    def Display(self):
        print("Stack elements are: ", end="")
        print(self.S)
    
def isValid(maze, path , x, y):
    if 0 <= x < len(maze) and 0 <= y < len(maze[0]) and \
            maze[x][y] == 0 and (x, y) not in path:
            return True
    return False
def find_path(maze, start, end):
    stack = Stack()
    path = []
    stack.Push(start)
    path.append(start)
    while not stack.isEmpty():
        current = stack.Peek()
        if current == end:
            return path
        x, y = current
        found_next = False
        for move in [(x,y+1), (x+1,y), (x,y-1), (x-1,y)]:
            nx, ny = move
            if isValid(maze, path, nx, ny):
                stack.Push((nx, ny))
                path.append((nx, ny))
                found_next = True
                break
        if not found_next:
            stack.Pop()  # Backtrack if no valid moves found
            path.pop()
            return None
def print_maze(maze):
    for i in range(len(maze)):
        for j  in range(len(maze[0])):
            if maze[i][j] == 0:
                print(".", end="")
            else:
                print("1", end="")
    print()

def print_maze_with_path(maze, path):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if (i, j) in path:
                print("S", end="")
            elif maze[i][j] == path[-1]:
                print("E", end="")
            elif maze[i][j] == 0:
                print("*", end="")
            else:
                print("1", end="")
    print()
            

# Example usage
maze = [[0, 0, 0, 1, 0, 0, 0 ,0],
        [0, 1, 0, 1, 1, 0, 1, 0],
        [0, 1, 0, 0, 0, 0, 1, 1],
        [0, 1, 1, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 1, 1, 1, 0],
        [1, 0, 1, 0, 0, 0, 1, 0],
        [1, 0, 1, 0, 0, 0, 1, 0],
        [0, 0, 1, 0, 0, 0, 1, 0]]
start = (0, 0)  # Starting point
end = (7, 7)    # Ending point
path = find_path(maze, start, end)

print("Original Maze:")
print_maze(maze)
print("Solved Path:")
if path:
    print_maze_with_path(maze, path)
else:
    print("No path found")
            
                

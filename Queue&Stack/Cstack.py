from node import Node

class ContiguousStack:
    def __init__(self, N):
        """
        Constructor
        This is a simple stack 
        """
        self.N = N #Maximum number of elements
        #The bottom is fixed at 0
        self.top = -1 #Position of the top of the stack
        self.array = N*[None] #Empty vector of length N.
        
    def isEmpty(self):
        """
        This method returns True if the stack is empty.
        When the stack is empty, both the start and the top are -1
        """
        return self.top == -1
    
    def __len__(self):
        """
        This method returns the length of the vector.
        The vector is defined from 0 to top. 
        """
        if self.isEmpty():
            return 0
        else:
            return self.top + 1 
    
    def isFull(self):
        """
        This function returns True if the stack is full.
        The stack is full when its length is equal to the maximum number of elements.
        """
        return len(self) == self.N
    
    
    def push(self, value):
        """
        This method inserts a value at the top of the stack.
        """
        if self.isFull(): 
            raise Exception("The stack is full")
        else:
            self.top += 1
            self.array[self.top] = value
            
    def peek(self):
        """
        This method returns the value at the top of the stack.
        """
        if self.isEmpty():
            raise Exception("The stack is empty")        
        else:
            return self.array[self.top]
        
    def pop(self):
        """
        This method removes and returns the value at the top of the stack.
        """        
        if self.isEmpty():
            raise Exception("Can't pop from empty stack")        
        else:
            element = self.peek()
            self.top -= 1
            return element
    
    def destroy(self):
        """
        This method clears the stack.
        """
        self.top = -1
        
    def __repr__(self):
        """
        Representation of the stack as string
        """
        return str(self.array[:self.top+1])
    

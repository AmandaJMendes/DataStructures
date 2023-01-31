from node import Node

class LinkedStack:
    def __init__(self):
        """
        Constructor
        This is a linked stack 
        """
        self.top = None #Points to the top node of the stack
        self.length = 0 #Length of the stack
        
    def isEmpty(self):
        """
        This method returns True if the stack is empty.
        """
        return not self.length
    
    def __len__(self):
        """
        This method returns the length of the vector.
        The vector is defined from 0 to top. 
        """
        return self.length
    
    def push(self, value):
        """
        This method inserts a value at the top of the stack.
        """
        if self.isEmpty():
            self.top = Node(value, None)
        else:
            new = Node(value, self.top)
            self.top = new
        self.length += 1
            
    def peek(self):
        """
        This method returns the value at the top of the stack.
        """
        if self.isEmpty():
            raise Exception("The stack is empty")        
        else:
            return self.top.value
        
    def pop(self):
        """
        This method removes and returns the value at the top of the stack.
        """        
        if self.isEmpty():
            raise Exception("Can't pop from empty stack")        
        else:
            element = self.peek()
            self.top  = self.top.next
            self.length -= 1
            return element
    
    def destroy(self):
        """
        This method clears the stack.
        """
        self.top = None
        self.length = 0
        
    def __repr__(self):
        """
        Representation of the stack as string
        """
        node = self.top
        s = ""
        for i in range(self.length):
            if i == self.length-1:
                s = str(node.value) + s
            else:
                s = ", " + str(node.value)  + s
            node = node.next
        return "[" + s + "]"

from node import Node

class LinkedQueue:
    def __init__(self):
        """ 
        Constructor
        This is a linked queue 
        """
        self.front = None #Points to the first node
        self.rear = None #Points to the last node
        self.length = 0 #Length of the queue
        
    def isEmpty(self):
        """
        This method returns True if the queue is empty.
        """
        return not self.length
    
    def __len__(self):
        """
        This method returns the length of the vector.
        The vector is defined from front to rear. 
        """
        return self.length
    
    def push(self, value):
        """
        This method inserts a value at the end of the queue.
        """
        if self.isEmpty():
            self.rear = self.front = Node(value, None)
        else:
            new = Node(value, None)
            self.rear.next = new
            self.rear = new
        self.length += 1
            
    def peek(self):
        """
        This method returns the first value in the queue.
        """
        if self.isEmpty():
            raise Exception("The stack is empty")        
        else:
            return self.front.value
        
    def pop(self):
        """
        This method removes and returns the first value in the queue.
        """    
        if self.isEmpty():
            raise Exception("Can't pop from empty stack")        
        else:
            element = self.peek()
            self.front  = self.front.next
            self.length -= 1
            return element
    
    def destroy(self):
        """
        This method clears the queue.
        """
        self.front = None
        self.rear = None
        
        self.length = 0
        
    def __repr__(self):
        """
        Representation of the queue as a string.
        """
        l = "["
        node = self.front
        for i in range(self.length):
            if i == self.length-1:
                l= l+ str(node.value)
            else:
                l = l+str(node.value)+", "
            node = node.next
        l = l + "]"
        return l
from node import Node

class ContiguousQueue:
    def __init__(self, N):
        """
        Constructor
        This is a contiguous queue
        """
        self.N = N #Maximum number of elements, upper limit
        #The lower limit is 0
        self.front = self.rear = -1 #Positions of the front and rear of the queue
        self.array = N*[None] #Empty vector of length N.
        
    def isEmpty(self):
        """
        This method returns True if the queue is empty.
        When the queue is empty, both the start and the top are -1
        """
        return self.rear == -1
    
    def __len__(self):
        """
        This method returns the length of the vector.
        The vector is defined from position front to position rear. 
        """
        if self.isEmpty():
            return 0
        else:
            if self.front > self.rear:
                return (self.N - self.front) + self.rear + 1
            else:
                return (self.rear - self.front + 1)
            return self.rear + 1 
    
    def isFull(self):
        """
        This function returns True if the queue is full.
        The queue is full when its length is equal to the maximum number of elements.
        """
        return len(self) == self.N
    
    
    def push(self, value):
        """
        This method inserts a value at the end of the queue.
        """
        if self.isFull(): 
            raise Exception("The stack is full")
        else:
            if self.isEmpty():
                self.front = self.rear = 0
            else:   
                if self.rear == self.N - 1:
                    self.rear = 0
                else:
                    self.rear += 1
            self.array[self.rear] = value
            
    def peek(self):
        """
        This method returns the first value in the queue.
        """
        if self.isEmpty():
            raise Exception("The stack is empty")        
        else:
            return self.array[self.front]
        
    def pop(self):
        """
        This method removes and returns the first value in the queue.
        """        
        if self.isEmpty():
            raise Exception("Can't pop from empty stack")        
        else:
            element = self.peek()
            if len(self) == 1:
                self.front = self.rear = -1
            else:
                if self.front == self.N - 1:
                    self.front = 0
                else:
                    self.front += 1
            return element
    
    def destroy(self):
        """
        This method clears the queue.
        """
        self.rear = self.front = -1
        
    def __repr__(self):
        """
        Representation of the queue as a string.
        """
        if self.front > self.rear:
            return str(self.array[self.front:] + self.array[:self.rear+1])
        else:
            return str(self.array[self.front:self.rear+1])
    

class MyList:
    def __init__(self, N):
        """
        Constructor
        
        This is a simple list 
        """
        self.N = N #Maximum number of elements
        self.start = self.end = -1 #Positions of the start and the end of the list
        #Start and end may vary from 0 to N-1
        self.array = N*[None] #Empty vector of length N.
        
    def isEmpty(self):
        """
        This method returns True if the list is empty.
        When the list is emṕty, both the start and the end are -1
        """
        return self.start == -1 and self.end == -1
    
    def __len__(self):
        """
        This method returns the length of the vector.
        The vector is defined from position start to position end. 
        """
        if self.isEmpty():
            return 0
        else:
            return self.end - self.start + 1 
    
    def isFull(self):
        """
        This function returns True if the list is full.
        The list is full when its length is equal to the maximum number of elements.
        """
        return len(self) == self.N
    
    
    def insert(self, value, pos):
        """
        This method inserts a value in a given position of the list.
        The first position of the list is 1.
        
        THIS IS NOT OPTIMIZED
        """
        if self.isFull(): 
            raise Exception("The list is full")

        elif not (1 <= pos <= len(self)+1):
            #Prevent the user from inserting an element in a position i without
            #filling the previous position (i-1)
            raise Exception(f"Try a position from 1 to {len(self)+1}")
        
        elif self.isEmpty():
            #Point start and end to the first position of the list
            #The element will be inserted later in the function, keep reading
            self.start = self.end = 0
            
        else:
            #If no exception was raised and the list is not empty, move the element(s) in the list
            #in order to open a gap for the new value
            for i in range(self.end+1, self.start + pos - 1, -1):
                #Move the values to the right
                self.array[i] = self.array[i-1]
            self.end += 1 #Increase the end position by one (move 1 position to the right)
            
        #If and exception is raised, this line will not be executed    
        self.array[self.start+pos-1] = value #Insert the new value
            
        
    def remove(self, pos):
        """
        This method removes a value from a given position of the list.
        The first position of the list is 1.
        
        THIS IS NOT OPTIMIZED
        """        
        if self.isEmpty():
            raise Exception("Can't remove from empty list")
            
        elif not(1 <= pos <= len(self)):
            #Prevent the user from trying to remove a value from a position
            #that is not in the range of the list
            raise Exception(f"Try a position from 1 to {len(self)}")
        
        else:
            #If no exception was raised, move the element(s) in the list in order to fill
            #the gap left by the removed value
            for i in range(self.start+pos-1, self.end):
                #Move the values to the left
                self.array[i] = self.array[i+1]
                
            if len(self) == 1:
                #If the length of the list was 1, now it's empty
                self.start = self.end = -1  
            else:
                #Decrease the end position by one (move 1 position to the left)
                self.end -= 1

    
    def search(self, value):
        """
        This method searches linearly for a value in the list.
        If the value is found, this method returns the position of the value (1 to N).
        Otherwise, it doesn't return anything (returns None).
        """
        for i in range(self.start, self.end+1):
            if self.array[i] == value:
                return i+1
    
    def clear(self):
        """
        This method clears the list by assigning all its values to None
        """
        for i in range(self.start, self.end+1):
            self.array[i] = None
        self.start = self.end = -1
        
    def __repr__(self):
        """
        Representation of the list as string
        """
        return str(self.array[self.start:self.end+1])
    
    def __getitem__(self, pos):
        """
        Get item in position pos (from 1 to N)
        """
        if self.isEmpty():
            raise Exception(f"The list is empty")
        elif 1 <= pos <= len(self):
            return self.array[self.start + pos - 1]
        else:
            raise Exception(f"Try a position from 1 to {len(self)}")
    
if __name__ == "__main__":
    from TAD import Product
    
    l = MyList(4)
    
    p0 = Product(0, "a", 10.0)
    p1 = Product(1, "b", 10.5)
    p2 = Product(2, "c", 10.8)
    p3 = Product(3, "d", 10.2)
    p4 = Product(4, "e", 10.0)
    
    print("Inserting in position 1")
    l.insert(p0, 1)
    print(f"New list: {l}\n")

    print("Removing in position 1")
    l.remove(1)
    print(f"New list: {l}\n")

    print("Inserting in position 1")
    l.insert(p1, 1)
    print(f"New list: {l}\n")

    print("Inserting in position 2")
    l.insert(p2, 2)
    print(f"New list: {l}\n")

    print("Removing all the values")
    l.clear()
    print(f"New list: {l}\n")

    print("Inserting in position 1")
    l.insert(p3, 1)
    print(f"New list: {l}\n")

    print("Inserting in position 1")
    l.insert(p0, 1)
    print(f"New list: {l}\n")

    print("Inserting in position 3")
    l.insert(p4, 3)
    print(f"New list: {l}\n")

    print("Removing in position 1")
    l.remove(1)
    print(f"New list: {l}\n")

    print("Inserting in position 1")
    l.insert(p0, 1)
    print(f"New list: {l}\n")

    print("Inserting in position 4")
    l.insert(p1, 4)
    print(f"New list: {l}\n")

    print("Product 0 is in: ", l.search(p0), '\n')

    print("Product 4 is in: ", l.search(p4), '\n')

    print("Product 2 is in: ", l.search(p2), '\n')

    print("Product 3 is in: ", l.search(p3), '\n')

    print("Removing in position 4")
    l.remove(4)
    print(f"New list: {l}\n")

    print("Removing in position 2")
    l.remove(2)
    print(f"New list: {l}\n")

    print("Removing in position 1")
    l.remove(1)
    print(f"New list: {l}\n")

    print("Removing in position 1")
    l.remove(1)
    print(f"New list: {l}\n")

    try: #An excpetion will be raised because the list is empty
        print("Removing in position 1")
        l.remove(1)
        print(f"New list: {l}\n")
    except:
        print ("AN EXCEPTION OCCURED\n")

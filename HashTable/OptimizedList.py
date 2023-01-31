from MyList import MyList

class OptimizedList(MyList):
    def __init__(self, N):
        """
        Constructor
        
        This is a list in which the insert and remove methods are optimized
        """
        MyList.__init__(self, N)
    
    def closeToStart(self, pos):
        """
        This method returns True if the position is closer to the beginning of the *non-empty*
        list than it is from its end. 
        """
        return (pos  <= len(self) - pos) and (self.end != self.N - 1)
    
    def insert(self, value, pos):
        """
        This method inserts a value in a given position of the list.
        The first position of the list is 1.
        """        
        if self.isFull():
            raise Exception("The list is full")

        elif not (1 <= pos <= len(self)+1):
            #Prevent the user from inserting an element in a position i without
            #filling the previous position (i-1)
            raise Exception(f"Try a position from 1 to {len(self)+1}")
        
        elif self.isEmpty():
            #Point start and end to the position in the middle of the vector
            #The element will be inserted later in the function, keep reading
            self.start = self.end = self.N//2
            
        else:
            #If no exception was raised and the list is not empty, move the element(s) and/or the start
            #and end position of the list
            if pos == 1 and self.start != 0:
                #If the insertion is in the beginning of the list and there is space to the left,
                #there is no need for moving the values
                self.start -= 1 #Decrease the start position by one (move 1 position to the left)
            elif pos == len(self) + 1 and self.end != self.N -1:
                #If the insertion is in the end of the list and there is space to the right,
                #there is no need for moving the values
                self.end += 1 #Increase the end position by one (move 1 position to the right)
            else:
                #If the position of the new value is somewhere else, some values need to be moved
                if (not self.closeToStart(pos) or self.start == 0) and (self.end != self.N-1):
                    #If the position is closer to the end of the list, move values to the right
                    #If the start is in 0, there is no choice other than inserting in the end
                    #of the list, even if the position is closer to the start.
                    for i in range(self.end+1, self.start + pos - 1, -1):
                        self.array[i] = self.array[i-1]
                    self.end += 1 #Increase the end position by one (move 1 position to the right)
                else:
                    #If the position is closer to the start of the list and the start is
                    #not 0 (there is still space to the left), move values to the left
                    for i in range(self.start, self.start+pos-1):
                        self.array[i-1] = self.array[i]
                    self.start -= 1 #Decrease the start position by one (move 1 position to the left)         
        #If and exception is raised, this line will not be executed  
        self.array[self.start+pos-1] = value #Insert the new value
        
    
    def remove(self, pos):
        """
        This method removes a value from a given position of the list.
        The first position of the list is 1.
        """   
        if self.isEmpty():
            raise Exception("Can't remove from empty list")
            
        elif not(1 <= pos <= len(self)):
            #Prevent the user from trying to remove a value from a position
            #that is not in the range of the list
            raise Exception(f"Try a position from 1 to {len(self)}")
        
        else:
            #If no exception was raised, remove the value from the list and move the other
            #elements to fill the gap if needed
            if pos == 1:
                #Remove the first element by moving the start to the right
                self.start += 1
                
            elif pos == len(self):
                #Remove the first element by moving the end to the left
                self.end -=1
            
            #If the position of the new value is somewhere else, some values need to be moved
            elif self.closeToStart(pos):
                #If the position is close to the start, move previous values to the left
                for i in range(self.start+pos-1, self.start, -1):
                    self.array[i] = self.array[i-1]
                self.start += 1 #Move the start to the right
                
            else:
                #If the position is close to the end, move following values to the left
                for i in range(self.start+pos-1, self.end):
                    self.array[i] = self.array[i+1]
                self.end -= 1 #Move the start to the left
                    
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


    
    
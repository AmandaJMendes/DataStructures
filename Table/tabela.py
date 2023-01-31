class Table:
    def __init__(self, Nmax):
        """
        Contiguous table with all the basic operations:
        - Create
        - Insert
        - Query
        - Remove
        - Destroy
        """
        self.Nmax = Nmax
        self.key = [None] * Nmax 
        self.value = [None] * Nmax 
        self.size = 0
        
    def __len__(self):
        return self.size
    
    def isEmpty(self):
        return self.size == 0
    
    def isFull(self):
        return self.size == self.Nmax 
    
    def search(self, key):
        """
        Linear search
        """
        for i in range(self.size):
            if key == self.key[i]:
                return i+1
            
    def query(self, key):
        idx = self.search(key)
        if idx: #1 <= idx <= self.size
            return self.value[idx-1]  #0 <= index in self.value <= self.size-1
    
    def insert(self, key, value):
        idx = self.search(key)
        if idx: #Modify 
            self.value[idx-1] = value
            return True
        else: #Add
            if not self.isFull():
                self.key[self.size] = key
                self.value[self.size] = value
                self.size += 1
                return True
    
    def remove(self, key):
        idx = self.search(key)
        if idx:
            if self.size > 1 and self.size != idx:
                #If there is only 1 element or the element to be removed is the last one,
                #there is no need to move the other elements
                for i in range(idx, self.size):
                    self.key[i - 1] = self.key[i]
                    self.value[i - 1] = self.value[i]
            self.size -= 1
            return True
    
    def destroy(self):
        self.size = 0
        
    def __str__(self):
        table = ""
        for i in range(self.size):
            table+= f"{{{self.key[i]}, {self.value[i]}}};"

        return table[:-1]

                
    
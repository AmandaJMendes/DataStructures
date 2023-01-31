from tabela import Table

class OptimizedTable(Table):
    def __init__(self, Nmax):
        """
        Contiguous table inherited from Table
        This table is always sorted and the search method is binary search
        """
        Table.__init__(self, Nmax)
        
    def search(self, key):
        """
        Binary search
        """
        if not self.isEmpty():
            start = 0
            end = self.size-1
            n = (start + end)//2
            while self.key[n] != key:
                if start == end:
                    return None
                else:
                    if self.key[n] > key:
                        end = max(n-1, 0)
                    else:
                        start = min(n+1, self.size-1)
                    n = (start + end)//2
            return n + 1
    
    def insert(self, key, value):
        """
        This method ensures that the table is kept sorted
        """
        idx = self.search(key)
        if idx:
            self.value[idx-1] = value
            return True
        else:
            if not self.isFull():  
                k = 0
                for i in range(self.size-1, -1, -1):
                    if key < self.key[i]:
                        self.key[i+1] = self.key[i]
                        self.value[i+1] = self.value[i]
                    else:
                        k = i + 1
                        break
                        
                self.key[k] = key
                self.value[k] = value       
                self.size += 1
                return True
            

            

from OptimizedList import OptimizedList #Contiguidade
from EncadeamentoDupla import LinkedList #Encadeamento

class HashTable:
    def __init__(self, Nmax):
        self.regs = OptimizedList(Nmax)
        self.Nmax = Nmax
        self.size = 0
        for i in range(Nmax):
            self.regs.insert(LinkedList(), i+1)
            
    def __len__(self):
        return self.size
    
    def isEmpty(self):
        return self.size == 0
    
    def isFull(self):
        return self.size == self.Nmax
    
    def search(self, key):
        idx = key%self.Nmax+1
        l = self.regs[idx]
        for i, node in enumerate(l):
            if node.value[0] == key:
                return (idx, i+1)

    def insert(self, key, value):
        idx = self.search(key)
        if idx: 
            self.regs[idx[0]][idx[1]].value = (key, value)
            return True
        else:
            if not self.isFull():
                idx = key%self.Nmax+1
                self.regs[idx].insert((key, value), 1)
                self.size += 1
                return True

    def query(self, key):
        idx = self.search(key)
        if idx: 
            return self.regs[idx[0]][idx[1]].value[1]  
    
    def remove(self, key):
        idx = self.search(key)
        if idx:
            self.regs[idx[0]].remove(idx[1])
            self.size -= 1
            return True
    
    def destroy(self):
        self.size = 0
        for i in range(self.Nmax):
            self.regs[i+1].clear()
            
    def __str__(self):
        table = "Position\n"
        for i in range(self.Nmax):
            table+= f"   {i+1}      "
            table+=(len(str(self.Nmax))-len(str(i+1)))*" "
            for j in self.regs[i+1]:
                table+=f"{{{j.value[0]}, {j.value[1]}}} "
            table+="\n"

        return table[:-1]


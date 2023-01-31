class Node:
    def __init__(self, value, next_node):
        """
        Constructor
        This is a node 
        """
        self.value = value #Value
        self.next = next_node #Points to next node or None     
    
    def __repr__(self):
        """
        Representation of the node as a string
        """
        return f"{self.value}"
    
class LinkedList:
    def __init__(self):
        """
        Constructor
        This is a linked list
        ##CRIA
        """
        self.start = None #Points to first node
        self.length = 0 #Length of the list
        
    def __len__(self):
        """
        This method returns the length of the list
        """
        return self.length
    
    def __getitem__(self, pos):
        """
        This method returns the value of the node in position pos (from 1 to length of the list)
        ##Valor(posição)
        """
        if not self.start:
            raise Exception(f"The list is empty")
        elif pos > self.length: 
            raise Exception(f"Try a position from 1 to {len(self)}")
        else:
            node = self.start
            for i in range(pos-1): 
                node = node.next
            return node
                
    def __repr__(self):
        """
        Representation of the list as a string
        """
        l = "["
        node = self.start
        for i in range(self.length):
            if i == self.length-1:
                l= l+ str(node.value)
            else:
                l = l+str(node.value)+", "
            node = node.next
        l = l + "]"
        return l
    
    def insert(self, value, pos):
        """
        This method inserts value in position pos (from 1 to length of the list + 1)
        ##Insere(valor, posição)
        """
        if 1 <= pos <= self.length + 1:
            if not self.start:
                new = Node(value, None)
                self.start = new
            else:
                if pos == 1:
                    new = Node(value, self.start)
                    self.start = new
                elif pos > self.length:
                    new = Node(value, None)
                    self[pos-1].next = new
                else: 
                    new = Node(value, self[pos])
                    self[pos-1].next = new
            self.length+=1
        else:
            raise Exception(f"Try a position from 1 to {len(self)+1}")
            
    def remove(self, pos):
        """
        This method removes the node in position pos (from 1 to length of the list) from the list
        ##Remove(posição)
        """
        if not self.start:
            raise Exception("Can't remove from empty list")
            
        elif not(1 <= pos <= self.length):
            raise Exception(f"Try a position from 1 to {len(self)}")
        
        else:
            if pos == 1:
                self.start = self.start.next
            elif pos == self.length:
                self[pos-1].next = None
            else:
                node = self[pos-1]
                node.next = node.next.next
            self.length -= 1
    
    def search(self, value):
        """
        This method returns a list of positions (from 1 to length of the list) where value is found
        ##Posição(valor)
        """
        idxs = []
        node = self.start
        for i in range(self.length):
            if node.value == value:
                idxs.append(i+1)
            node = node.next
        return idxs

    def clear(self):
        """
        This method clears the list. It makes the list empty by pointing start to None and resetting the length to 0.
        ##Destroi
        """
        self.start = None
        self.length = 0
    

    
    
    
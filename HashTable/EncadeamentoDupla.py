class Node:
    def __init__(self, value, next_node, previous_node):
        """
        Constructor
        This is a node 
        """
        self.value = value #Value
        self.next = next_node #Points to next node or None
        self.prev = previous_node #Points to previous node or None
    
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
        self.end = None #Points to the last node
        self.length = 0 #Length of the list
        
    def __len__(self):
        """
        This method returns the length of the list
        """
        return self.length
    
    def __getitem__(self, pos):
        """
        This method returns the value of the node in position pos (from 1 to length of the list)
    
        It iterates from either start to end or from end to start, depending on the position
        ##Valor(posição)
        """
        if not self.start:
            raise Exception(f"The list is empty")
        elif pos > self.length: 
            raise Exception(f"Try a position from 1 to {len(self)}")
        else:
            if pos <= len(self)/2:
                node = self.start 
                for i in range(pos-1): 
                    node = node.next
            else:
                node = self.end
                for i in range(len(self) - pos):
                    node = node.prev
            return node
                
    def __repr__(self, reverse = False):
        """
        Representation of the list as a string
        """
        l = "["
        node = self.end if reverse else self.start 
        for i in range(self.length):
            if i == self.length-1:
                l= l+ str(node.value)
            else:
                l = l+str(node.value)+", "
            node = node.prev if reverse else node.next
        l = l + "]"
        return l
        
    def insert(self, value, pos):
        """
        This method inserts value in position pos (from 1 to length of the list + 1)
        ##Insere(valor, posição)
        """
        if 1 <= pos <= self.length + 1:
            if not self.start:
                new = Node(value, None, None)
                self.start = self.end = new
            else:
                if pos == 1:
                    new = Node(value, self.start, None)
                    self.start.prev = new
                    self.start = new
                elif pos > self.length:
                    new = Node(value, None, self.end)
                    self.end.next = new
                    self.end = new
                else:
                    node = self[pos]
                    new = Node(value, node, node.prev)
                    node.prev.next = node.prev = new
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
                if not self.length:
                    self.start.prev = None
            elif pos == self.length:
                self.end = self.end.prev
                self.end.next = None
            else:
                node = self[pos]
                node.prev.next = node.next
                node.next.prev = node.prev
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
        self.end = None
        self.length = 0
        
    def reverse(self):
        """
        This method reverses the list.
        """
        node = self.start
        for i in range(len(self)):
            temp = node.next
            node.next = node.prev
            node.prev = temp
            node = temp
            
        temp = self.start
        self.start = self.end
        self.end = temp
    
    def printReversed(self):
       """
       This method prints the list in reverse
       """
       print (self.__repr__(reverse = True))
        
          
    def isEqual(self, list2):
        """
        This method returns whether list2 is equal to this list 
        """
        if self.length != len(list2):
            return False
        
        elif self.length == 0:
            return True    
        else:
            node1 = self.start
            node2 = list2[1]
            for i in range(self.length):
                if node1.value != node2.value:
                    return False
                else:
                    node1 = node1.next
                    node2 = node2.next
            return True
            
    def __iter__(self):
        self.node_iter = self.start
        return self
    
    def __next__(self):
        if self.node_iter:
            node = self.node_iter
            self.node_iter = self.node_iter.next
            return node
        else:
            raise StopIteration
        
    
    
    
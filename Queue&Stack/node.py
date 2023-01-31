class Node:
    def __init__(self, value, next_node, previous_node = None):
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

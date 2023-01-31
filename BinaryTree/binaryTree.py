class Node:
    def __init__(self, value, left = None, right = None, parent = None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
        
    def __repr__(self):
        return str(self.value)

class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0
    
    def other_search(self, value):
        """
        Just practicing a search function without recursion.
        """
        pile = [self.root]
        while pile:
            node = pile.pop()
            if node.value == value:
                return node
            else:
                if node.right:
                    pile.append(node.right)
                if node.left:
                    pile.append(node.left)
                    
    def mysearch(self, value, root, method, left_param, show):
        if root:
            if method == "pre":
                if show:
                    print("Visiting node", root.value)
                if root.value == value:
                    return root
                if left_param:
                    left = self.mysearch(value, root.left, method, left_param, show)
                    if left:
                        return left
                    right = self.mysearch(value, root.right, method, left_param, show)
                    if right:
                        return right
                else:
                    right = self.mysearch(value, root.right, method, left_param, show)
                    if right:
                        return right
                    left = self.mysearch(value, root.left, method, left_param, show)
                    if left:
                        return left                    
                
            elif method == "post":
                if left_param:
                    left = self.mysearch(value, root.left, method, left_param, show)
                    if left:
                        return left
                    right = self.mysearch(value, root.right, method, left_param, show)
                    if right:
                        return right
                else:
                    right = self.mysearch(value, root.right, method, left_param, show)
                    if right:
                        return right
                    left = self.mysearch(value, root.left, method, left_param, show)
                    if left:
                        return left                    
                if show:
                    print("Visiting node", root.value)
                if root.value == value:
                    return root
                
            else:
                if left_param:
                    left = self.mysearch(value, root.left, method, left_param, show)
                    if left:
                        return left
                else:
                    right = self.mysearch(value, root.right, method, left_param, show)
                    if right:
                        return right
                if show:
                    print("Visiting node", root.value)
                if root.value == value:
                    return root
                if left_param:
                    right = self.mysearch(value, root.right, method, left_param, show)
                    if right:
                        return right
                else:
                    left = self.mysearch(value, root.left, method, left_param, show)
                    if left:
                        return left
                    
    def search(self, value, method = "pre", left = True, show = False):
        """
        pre, post, in -order
        """
        if method in ["pre", "post", "in"]:
            return self.mysearch(value, self.root, method, left, show)
        else:
            print("Invalid method.")
            
    def insert(self, valChild, valParent = None, left = True):
        if valChild:
            if not (self.size or valParent):
                self.root = Node(valChild)
                self.size += 1
            else:
                parent = self.search(valParent)
                if parent:
                    if left:
                        if not parent.left:
                            parent.left = Node(valChild, parent = parent)
                            self.size += 1
                        else:
                            print("Left child already exists.")
                    else:
                        if not parent.right:
                            parent.right = Node(valChild, parent = parent)
                            self.size += 1
                        else:
                            print("Right child already exists.")
                else:
                    print("Parent was not found.")
        else:
            print("Invalid value for a node.")
            
    def remove(self, value):
        node = self.search(value)
        if not node:
            print ("Node was not found.")
        elif not (node.left or node.right):
            if self.size == 1:
                self.root = None
            else:
                l_child = node.parent.left
                if l_child and l_child.value == value:
                    node.parent.left = None
                else:
                    node.parent.right = None
            self.size -= 1
        else:
            print("This is not a leaf node.")
            
    def printNodes(self, method = "pre", left = True):
        self.search(None, method, left, True)
        
if __name__ == "__main__":
    t = BinaryTree()
    t.insert(1)
    t.insert(2, 1)
    t.insert(3, 1, False)
    t.insert(4, 2)
    t.insert(5, 2, False)
    t.insert(6, 3)
    t.insert(7, 3, False)
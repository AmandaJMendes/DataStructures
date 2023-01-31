from binaryTree import BinaryTree
#Default search method = Pre-order (left first)

tree = BinaryTree()

print("\nInsert left child with data 10 to parent with data 1.")
tree.insert(10, 1)

print("\nInsert root with data 1.")
tree.insert(1, None)

print("\nSearch for child with data 1 (Pre-order / left first).")
print(tree.search(1, show = True))

print("\nInsert left child with data 2 to parent with data 3.")
tree.insert(2, 3)

print("\nInsert left child with data 2 to parent with data 1.")
tree.insert(2, 1)

print("\nInsert left child with data 3 to parent with data 1.")
tree.insert(3, 1)

print("\nInsert right child with data 3 to parent with data 1.")
tree.insert(3, 1, left = False)

print("\nInsert left child with data 4 to parent with data 2.")
tree.insert(4, 2)

print("\nInsert right child with data 7 to parent with data 3.")
tree.insert(7, 3, left = False)

print("\nWalk the tree (Pre-order / left first).")
tree.printNodes()

print("\nWalk the tree (Post-order / left first).")
tree.printNodes("post")

print("\nWalk the tree (In-order / left first).")
tree.printNodes("in")

print("\nWalk the tree (Pre-order / right first).")
tree.printNodes(left = False)

print("\nWalk the tree (Post-order / right first).")
tree.printNodes("post", left = False)

print("\nWalk the tree (In-order / right first).")
tree.printNodes("in", left = False)

print("\nRemove node with data 2.")
tree.remove(2)

print("\nRemove node with data 4.")
tree.remove(4)

print("\nSearch for child with data 4 (Pre-order / left first).")
print(tree.search(4, show = True))

print("\nSearch for child with data 7 (In-order / right first).")
print(tree.search(7, method = "in", left = False, show = True))

print("\nRemove node with data 2.")
tree.remove(2)

print("\nWalk the tree (Pre-order / left first).")
tree.printNodes()


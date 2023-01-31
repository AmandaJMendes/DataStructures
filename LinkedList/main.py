from Encadeamento import LinkedList

l = LinkedList()
print(f"Linked list is initialized: {l}\n")

print("Inserting in position 1")
l.insert(0, 1)
print(f"New list: {l}\n")

print("Removing in position 1")
l.remove(1)
print(f"New list: {l}\n")

print("Inserting in position 1")
l.insert(1, 1)
print(f"New list: {l}\n")

print("Inserting in position 2")
l.insert(2, 2)
print(f"New list: {l}\n")

print("Removing all the values")
l.clear()
print(f"New list: {l}\n")

print("Inserting in position 1")
l.insert(3, 1)
print(f"New list: {l}\n")

print("Inserting in position 1")
l.insert(0, 1)
print(f"New list: {l}\n")

print("Value 4 is in: ", l.search(4), '\n')

print("Value 0 is in: ", l.search(0), '\n')

print("Inserting in position 3")
l.insert(4, 3)
print(f"New list: {l}\n")

print("Removing in position 1")
l.remove(1)
print(f"New list: {l}\n")

print("Inserting in position 1")
l.insert(0, 1)
print(f"New list: {l}\n")

print("Inserting in position 4")
l.insert(0, 4)
print(f"New list: {l}\n")

print("Value 0 is in: ", l.search(0), '\n')

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

print("Removing in position 1")
l.remove(1)
print(f"New list: {l}\n")

        

from my_hash import HashTable

t = HashTable(10)

print(f"Hash table of size {len(t)}:\n{t}\n")

print("Remove key 10:")
t.remove(10)
print(f"Hash table of size {len(t)}:\n{t}\n")

print("Insert {2, 20}:")
t.insert(2, 20)
print(f"Hash table of size {len(t)}:\n{t}\n")

print("Insert {5, 30}:")
t.insert(5, 30)
print(f"Hash table of size {len(t)}:\n{t}\n")

print("Insert {0, 10}:")
t.insert(0, 10)
print(f"Hash table of size {len(t)}:\n{t}\n")

print("Query key 7:", t.query(7))

print("Search key 2:", t.search(2))

print("Search key 4:", t.search(4))

print("Remove key 2:")
t.remove(2)
print(f"Hash table of size {len(t)}:\n{t}\n")

print("Insert {55, 40}:")
t.insert(55, 40)
print(f"Hash table of size {len(t)}:\n{t}\n")

print("Query key 5:", t.query(5))

print("Query key 55:", t.query(55))

print("Search key 5:", t.search(5))

print("Search key 55:", t.search(55))

print("Remove key 0:")
t.remove(0)
print(f"Hash table of size {len(t)}:\n{t}\n")

print("Remove key 5:")
t.remove(5)
print(f"Hash table of size {len(t)}:\n{t}\n")

print("Destroy: ")
t.destroy()
print(f"Hash table of size {len(t)}:\n{t}\n")

print("Insert {2, 20}:")
t.insert(2, 20)
print(f"Hash table of size {len(t)}:\n{t}\n")

print("Insert {45, 40}:")
t.insert(45, 40)
print(f"Hash table of size {len(t)}:\n{t}\n")


from tabela import Table
from tabela_buscaBinaria import OptimizedTable

t1 = Table(5)
t2 = OptimizedTable(5)

print(f"Table 1 of size {len(t1)}: {t1}\nTable 2 of size {len(t2)}: {t2}\n")

print("Remove key 10:")
t1.remove(10)
t2.remove(10)
print(f"Table 1 of size {len(t1)}: {t1}\nTable 2 of size {len(t2)}: {t2}\n")

print("Insert {2, 20}:")
t1.insert(2, 20)
t2.insert(2, 20)
print(f"Table 1 of size {len(t1)}: {t1}\nTable 2 of size {len(t2)}: {t2}\n")

print("Insert {5, 30}:")
t1.insert(5, 30)
t2.insert(5, 30)
print(f"Table 1 of size {len(t1)}: {t1}\nTable 2 of size {len(t2)}: {t2}\n")

print("Insert {0, 10}:")
t1.insert(0, 10)
t2.insert(0, 10)
print(f"Table 1 of size {len(t1)}: {t1}\nTable 2 of size {len(t2)}: {t2}\n")

print("Query key 7:")
print(f"Table 1 of size {len(t1)}: {t1.query(7)}\nTable 2 of size {len(t2)}: {t2.query(7)}\n")

print("Query key 5:")
print(f"Table 1 of size {len(t1)}: {t1.query(5)}\nTable 2 of size {len(t2)}: {t2.query(5)}\n")

print("Search key 2:")
print(f"Table 1 of size {len(t1)}: {t1.search(2)}\nTable 2 of size {len(t2)}: {t2.search(2)}\n")

print("Search key 4:")
print(f"Table 1 of size {len(t1)}: {t1.search(4)}\nTable 2 of size {len(t2)}: {t2.search(4)}\n")

print("Remove key 2:")
t1.remove(2)
t2.remove(2)
print(f"Table 1 of size {len(t1)}: {t1}\nTable 2 of size {len(t2)}: {t2}\n")

print("Insert {3, 40}:")
t1.insert(3, 40)
t2.insert(3, 40)
print(f"Table 1 of size {len(t1)}: {t1}\nTable 2 of size {len(t2)}: {t2}\n")

print("Remove key 0:")
t1.remove(0)
t2.remove(0)
print(f"Table 1 of size {len(t1)}: {t1}\nTable 2 of size {len(t2)}: {t2}\n")

print("Remove key 5:")
t1.remove(5)
t2.remove(5)
print(f"Table 1 of size {len(t1)}: {t1}\nTable 2 of size {len(t2)}: {t2}\n")

print("Insert {2, 20}:")
t1.insert(2, 20)
t2.insert(2, 20)
print(f"Table 1 of size {len(t1)}: {t1}\nTable 2 of size {len(t2)}: {t2}\n")

print("Insert {4, 40}:")
t1.insert(4, 40)
t2.insert(4, 40)
print(f"Table 1 of size {len(t1)}: {t1}\nTable 2 of size {len(t2)}: {t2}\n")

print("Destroy: ")
t1.destroy()
t2.destroy()
print(f"Table 1 of size {len(t1)}: {t1}\nTable 2 of size {len(t2)}: {t2}\n")

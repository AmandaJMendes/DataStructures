from Cqueue import ContiguousQueue 
from Lqueue import LinkedQueue

cs = ContiguousQueue(10)
ls = LinkedQueue()


print(f"Contiguous queue of length {len(cs)}: {cs}")
print(f"Linked queue of length {len(ls)}: {ls}\n")


print("Inserting 1...")
cs.push(1)
ls.push(1)
print(f"Contiguous queue of length {len(cs)}: {cs}")
print(f"Linked queue of length {len(ls)}: {ls}\n")

print("Inserting 10...")
cs.push(10)
ls.push(10)
print(f"Contiguous queue of length {len(cs)}: {cs}")
print(f"Linked queue of length {len(ls)}: {ls}\n")

print("Peeking... ")
print(f"Front of contiguous queue of length {len(cs)}: {cs.peek()}")
print(f"Front of linked queue of length {len(ls)}: {ls.peek()}\n")

print("Removing...")
cs.pop()
ls.pop()
print(f"Contiguous queue of length {len(cs)}: {cs}")
print(f"Linked queue of length {len(ls)}: {ls}\n")

print("Inserting 2...")
cs.push(2)
ls.push(2)
print(f"Contiguous queue of length {len(cs)}: {cs}")
print(f"Linked queue of length {len(ls)}: {ls}\n")

print("Inserting 5...")
cs.push(5)
ls.push(5)
print(f"Contiguous queue of length {len(cs)}: {cs}")
print(f"Linked queue of length {len(ls)}: {ls}\n")

print("Removing...")
cs.pop()
ls.pop()
print(f"Contiguous queue of length {len(cs)}: {cs}")
print(f"Linked queue of length {len(ls)}: {ls}\n")

print("Removing...")
cs.pop()
ls.pop()
print(f"Contiguous queue of length {len(cs)}: {cs}")
print(f"Linked queue of length {len(ls)}: {ls}\n")

print("Inserting 20...")
cs.push(20)
ls.push(20)
print(f"Contiguous queue of length {len(cs)}: {cs}")
print(f"Linked queue of length {len(ls)}: {ls}\n")

print("Destroying...")
cs.destroy()
ls.destroy()
print(f"Contiguous queue of length {len(cs)}: {cs}")
print(f"Linked queue of length {len(ls)}: {ls}\n")
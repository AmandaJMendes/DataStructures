from TAD import Product
from MyList import MyList
from OptimizedList import OptimizedList
from time import time

p0 = Product(0, "a", 10.0)
p1 = Product(1, "b", 10.5)
p2 = Product(2, "c", 10.8)
p3 = Product(3, "d", 10.2)
p4 = Product(4, "e", 10.0)

ts = []

l_simple = MyList(4)
l_opt = OptimizedList(4)

for l, i in zip([l_simple, l_opt], ["WITHOUT OPTIMIZATION", "WITH OPTIMIZATION"]):
    print("\n---------", i, "---------\n")
    t0 = time()
    print("Inserting in position 1")
    l.insert(p0, 1)
    print(f"New list: {l}\n")

    print("Removing in position 1")
    l.remove(1)
    print(f"New list: {l}\n")

    print("Inserting in position 1")
    l.insert(p1, 1)
    print(f"New list: {l}\n")

    print("Inserting in position 2")
    l.insert(p2, 2)
    print(f"New list: {l}\n")

    print("Removing all the values")
    l.clear()
    print(f"New list: {l}\n")

    print("Inserting in position 1")
    l.insert(p3, 1)
    print(f"New list: {l}\n")

    print("Inserting in position 1")
    l.insert(p0, 1)
    print(f"New list: {l}\n")

    print("Inserting in position 3")
    l.insert(p4, 3)
    print(f"New list: {l}\n")

    print("Removing in position 1")
    l.remove(1)
    print(f"New list: {l}\n")

    print("Inserting in position 1")
    l.insert(p0, 1)
    print(f"New list: {l}\n")

    print("Inserting in position 4")
    l.insert(p1, 4)
    print(f"New list: {l}\n")

    print("Product 0 is in: ", l.search(p0), '\n')

    print("Product 4 is in: ", l.search(p4), '\n')

    print("Product 2 is in: ", l.search(p2), '\n')

    print("Product 3 is in: ", l.search(p3), '\n')

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
    
    try: #An excpetion will be raised because the list is empty
        print("Removing in position 1")
        l.remove(1)
        print(f"New list: {l}\n")
    except:
        print ("AN EXCEPTION OCCURED\n")
        
    ts.append(time()-t0)

print("Without optimization: ", ts[0])
print("With optimization: ", ts[1])

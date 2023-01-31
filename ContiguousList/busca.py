from MyList import MyList
import numpy as np

l = MyList(5)
l.insert(1,1)
l.insert(2,2)
l.insert(3,3)
l.insert(6,4)
l.insert(5,5)

def buscaBin(l, valor):
    n = int(np.ceil(len(l)/2))
    while not l[n] == valor:
        print(n)
        if not (1 < n < len(l)):
            return None
        if l[n]>valor:
            n = int(np.ceil(n/2))
        else:
            n = int(n+np.ceil((len(l) - n)/2))
    return l[n]
        
    
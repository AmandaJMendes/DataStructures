from Cqueue import ContiguousQueue
from Lqueue import LinkedQueue
from Cstack import ContiguousStack
from Lstack import LinkedStack
import random

def sortQueue(queue):
    s1 = LinkedStack()
    s2 = LinkedStack()

    for i in range(len(queue)):
        value = queue.pop()
        
        if len(s1) > 0 and value > s1.peek():
            while value > s1.peek():
                s2.push(s1.pop())
                if len(s1) == 0:
                    break
        elif len(s2) > 0 and value < s2.peek():
            while value < s2.peek():
                s1.push(s2.pop())
                if len(s2) == 0:
                    break 
        s1.push(value)
        
    for i in range(len(s2)):
        s1.push(s2.pop())
        
    for i in range(len(s1)):
        queue.push(s1.pop())
        
if __name__ == "__main__":
    cq = ContiguousQueue(10)
    lq = LinkedQueue()
    
    for i in range(3):
        for i in range(10):
            value = random.randint(-10, 10)
            cq.push(value)
            lq.push(value)

        print("Original contiguous queue: ", cq)
        sortQueue(cq)
        print("Sorted contiguous queue: ", cq)
        print("Original linked queue: ", lq)
        sortQueue(lq)
        print("Sorted linked queue: ", lq, "\n")
        
        cq.destroy()
        lq.destroy()

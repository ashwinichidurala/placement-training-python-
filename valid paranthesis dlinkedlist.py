#double linked list valid paranthesis
class Node:
    def __init__(self, u):
        self.data = u
        self.nxt = None
        self.prev = None

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
    def addback(self, x):
        if self.head is None:
            self.head = Node(x)
            self.tail = self.head
        else:
            t = Node(x)
            self.tail.nxt = t
            t.prev = self.tail
            self.tail = self.tail.nxt
    def display(self):
        t = self.head
        while t is not None:
            print(t.data, end="->")
            t = t.nxt
        print()
    def 
        




l1 = DLL()
l1.addback('[')
l1.addback('(')
l1.addback(')')
l1.addback(']')
l1.display()

        

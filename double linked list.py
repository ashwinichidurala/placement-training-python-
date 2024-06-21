#double linked list
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

    def addfront(self, x):
        if self.head is None:
            self.head = Node(x)
            self.tail = self.head
        else:
            t = Node(x)
            t.nxt = self.head
            self.head.prev = t
            self.head = t

    def display(self):
        t = self.head
        while t is not None:
            print(t.data, end="->")
            t = t.nxt
        print()

    def rev_display(self):
        t = self.tail
        while t is not None:
            print(t.data, end="->")
            t = t.prev
        print()
    def linearsearch(self,target):
        t1=self.head
        t2=self.tail
        while t1 != t2 and t1.prev != t2:
            if t1.data == target:
                print("Found")
                return
            if t2.data == target:
                print("Found")
                return
            t1 = t1.nxt
            t2 = t2.prev
    def even_oddlen(self):
        t1=self.head
        t2=self.tail
        while(t1!=t2 and t1!=t2.nxt):
            t1 = t1.nxt
            t2 = t2.prev
        if(t1==t2):
            print("odd")
        else:
            print("even")
    def ispalindrome(self):
        t1=self.head
        t2=self.tail
        while(t1!=t2 and t1!=t2.nxt):
            if(t1.data==t2.data):
                return "palindrome"
            t1 = t1.nxt
            t2 = t2.prev
        
        return "notpalindrome"           
        
    #printing middle to last elements first and first elements at last using fast and slow pointer
    """def changelinklist(self):
        f=self.head
        s=self.head
        while(f!=None):
            
            t1=t1.nxt.nxt
            t2=t2.nxt
        self.tail.nxt=self.head
        self.head.prev=self.nxt
        t1=self.prev
        t1.nxt=None
        self.prev=None
        self.head=s
        s.t=t1"""
    """def swapdata(self):
        f=self.head
        s=self.head
        while(f!=None and s!=None):
            f.data=s.data
            s.data=f.data"""
    def evod(self, node, es=0, os=0):
        if node is None:
            return es - os
        if node.data % 2 == 0:
            es += node.data
        else:
            os += node.data
        return self.evod(node.next, es, os)


        
        
            
            
            
            
        
        
        
             
            
        
        
        


l1 = DLL()
l1.addback(10)
l1.addfront(30)
l1.addback(50)
l1.addback(30)
#l1.addfront(10)
l1.display()
l1.rev_display()
l1.linearsearch(50)
l1.even_oddlen()
print(l1.ispalindrome())
result=l1.evod()

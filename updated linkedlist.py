class node:
    def __init__(self, u):
        self.data = u
        self.nxt = None

class sll:
    def __init__(self):
        self.head = None
        
    def display(self):
        t = self.head
        while(t != None):
            print(t.data, end="->")
            t = t.nxt
        print("None")

    def addback(self, x):
        if self.head is None:
            self.head = node(x)
        else:
            t = self.head
            while(t.nxt != None):
                t = t.nxt
            t.nxt = node(x)

    def addeven(self):
        t = self.head
        s = 0
        while(t != None):
            if t.data % 2 == 0:
                s += t.data
            t = t.nxt
        print(f"Sum of even numbers: {s}")

    def addfront(self, x):
        new_node = node(x)
        new_node.nxt = self.head
        self.head = new_node

    def isinlinkedlist(self, x):
        t = self.head
        while(t != None):
            if t.data == x:
                return "found"
            t = t.nxt
        return "not found"

    def midnode(self):
        s = self.head
        f = self.head
        if self.head != None:
            while(f != None and f.nxt != None):
                s = s.nxt
                f = f.nxt.nxt
            return s.data
        return None

    def sequence(self):
        if self.head is None:
            return 0
        
        max_len = 1
        current_len = 1
        t = self.head
        
        while(t.nxt != None):
            if t.data + 1 == t.nxt.data:
                current_len += 1
            else:
                if current_len > max_len:
                    max_len = current_len
                current_len = 1
            t = t.nxt
        
        if current_len > max_len:
            max_len = current_len
        
        return max_len

    def print_pairs(self):
        t1 = self.head
        while(t1 != None):
            t2 = t1.nxt
            while(t2 != None):
                print(t1.data,t2.data)
                t2 = t2.nxt
            t1 = t1.nxt
    def bubblesort(self):
        c=0
        T = self.head
        p=None
        while(T.nxt !=None):
            f=0
            t=self.head
            while(T.nxt !=p):
                if(t.data>t.nxt.data):
                    f=1
                    t.data,t.nxt.data=t.nxt.data,t.data
                t=t.nxt
                c=c+1
            if(f===0):
                break
            p=t
            t=t.nxt
            
                
        
        
            
            
        
            
                    
                
            
            
            
            
            
        
        

# Usage
l1 = sll()
l1.head = node(100)
l1.addback(200)
l1.addback(300)
l1.addback(400)
l1.addback(500)
l1.addback(600)
l1.addback(700)

l1.display()  
l1.addeven()  
print(l1.isinlinkedlist(60))  

print("Middle node:", l1.midnode())  

l1 = sll()
l1.head = node(100)
l1.addback(20)
l1.addback(30)
l1.addback(50)
l1.addback(60)
l1.addback(70)
l1.addback(90)

l1.display()
print(l1.sequence())



l1.print_pairs()

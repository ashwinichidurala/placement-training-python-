#linked list creation
class node:
    def __init__(self,u):
        self.data=u
        self.nxt=None
class sll:
    def __init__(self):
        self.head=None
        
    def display(self):
        s=0
        t=self.head
        while(t!=None):
            #adding all nodes in linked list
            #s=s+t.data
            print(t.data,end="->")
            t=t.nxt
    def addback(self,x):
        t=self.head
        while(t.nxt!=None):
            t=t.nxt
        t.nxt=node(x)
    def addeven(self):
        t=self.head
        s=0
        while(t.nxt!=None):
            if(t.data%2==0):
                s=s+t.data
    def addfront(self,x):
        t=node(x)
    def  isinlinkedlist(self,x):
        t=self.head
        while(t.nxt!=None):
            if(t.data==x):
                return "found"
            t=t.nxt
        return "notfound"
    #fast slow pointer for midnode finding
    def midnode(self,x):
        v=[]
        while(t.nxt!=None):
            v.append(t.data)
            t=t.nxt
        
    
            middleIdx = len(v) // 2
    
        return v[middleIdx]
    #longest number sequence in linkedlist
    def sequence(self,x):
        f=head.data
        s=head.data
        
        
        
        
        
    
    
            
                
                
            
        
            
            
        
        
            
            
        
        
        
        

        
l1=sll()
    
l1.head=node(10)
l1.addback(20)
l1.addback(30)
l1.addback(40)
l1.addback(50)
l1.addback(60)
l1.addback(70)

l1.display()
l1.addeven()
print(l1.isinlinkedlist(60))
    


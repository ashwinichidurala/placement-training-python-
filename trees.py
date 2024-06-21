#trees
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        

class Tree:
    def __init__(self):
        self.root = None

    def create(self, root, x):
        if root is None:
            return Node(x)
        elif x < root.data:
            root.left = self.create(root.left, x)
        else:
            root.right = self.create(root.right, x)
        return root

    def insert(self, x):
        self.root = self.create(self.root, x)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=' ')
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.data, end=' ')
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=' ')
    def sumofnodes(self,root):
        
        if root is None:
            return 0
        return root.data + self.sumofnodes(root.left)+self.sumofnodes(root.right)
        #only left sub treee sum
        #return root.data + self.sumofnodes(root.left)
    def sumofeven(self,root):
        if root is None:
            return 0
        
        if root.data % 2 == 0:
            return root.data + self.sumofeven(root.left) + self.sumofeven(root.right)
        
        return self.sumofeven(root.left) + self.sumofeven(root.right)
            
            
        
    
    def sumofodd(self,root):
        if root is None:
            return 0
        
        if root.data % 2 != 0:
            return root.data + self.sumofodd(root.left) + self.sumofodd(root.right)
        
        return self.sumofodd(root.left) + self.sumofodd(root.right)
        
    def absdiffevenoddsum(self,root):
    
        
        if root is None:
            return 0
        if root.data % 2 != 0:
            return root.data + self.sumofnode(root.left) + self.sumofnodes(root.right)
        return root.data - self.sumofnodes(root.left) + self.sumofnodes(root.right)

    def treeheight(self,root):
        if root is None:
            return 0
        return max(self.treeheight(root.left),self.treeheight(root.right))+1
    
    """def balancedtree(self,root):
        return abs(self.balancedtree(root.left)-self.balancedtree(root.right))<=1
    if(balancedtree(root)):
        print("balanced")
    else:
        print("not balanced")"""

    def countofleafnode(self,root):
        
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        return self.countofleafnode(root.left) + self.countofleafnode(root.right)

    
#-------------------------------check element present in binary tree if present print depth of the tree--------------------------------------------
    def present_depth(self,root,x):
        if root is None or root.data == x:
            return root
        elif x < root.data:
            return present_depth(root.left, x)
        else:
            return self.present_depth(root.right, x)

#--------------------------------depth of a  node----------------------------------------------------------------------------------------------------
        
     def depth(self,root):
         
    
        
       
        
        
        
        
            
        
        
            
           
        
        
        
        
        
        
        
            
        
if __name__ == "__main__":
    bt = Tree()
    bt.insert(10)
    bt.insert(5)
    bt.insert(15)
    bt.insert(2)
    bt.insert(7)
    bt.insert(1)
    bt.insert(3)

    
    bt.inorder(bt.root)
    print()
    bt.preorder(bt.root)
    print()
    bt.postorder(bt.root)
    print()
    print(bt.sumofnodes(bt.root))
    print()
    print(bt.sumofeven(bt.root))
    print()
    print(bt.sumofodd(bt.root))
    print()

    print(bt.absdiffevenoddsum(bt.root))
    print(bt.treeheight(bt.root))
    #print(bt.balancedtree(bt.root))
    print("count of leaf nodes")
    print(bt.countofleafnode(bt.root))
    print(bt.present_depth(bt.root,15))
    
    

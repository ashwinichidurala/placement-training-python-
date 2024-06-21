class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Binary_tree:
    def create_node(self, data):
        return Node(data)

    def insert(self, node, data):
        if node is None:
            return self.create_node(data)
        if data < node.data:
            node.left = self.insert(node.left, data)
        else:
            node.right = self.insert(node.right, data)
        return node

    def leftview(self, root, c, l):
        if root is None:
            return
        if c not in l:
            l.append(c)
            print(root.data, c)
        self.leftview(root.left, c + 1, l)
        self.leftview(root.right, c + 1, l)

    def rightview(self, root, c, l):
        if root is None:
            return
        if c not in l:
            l.append(c)
            print(root.data, c)
        self.rightview(root.right, c + 1, l)
        self.rightview(root.left, c + 1, l)
    

    """def top(self, root, c, l):
        if root is None:
            return l
        if c not in l:
            l[c] = root.data
        if c < 0 and c in l:
            if root.data > l[c]:
                l[c] = root.data
        self.top(root.left, c + 1, l)
        self.top(root.right, c - 1, l)
        
        return l"""
    def topview(self,root):
        if (root==None):
            return 
        d={}
        q=[(root,0)]
        while q:
            root=q[0][0]
            if(root.left!=None):
                q.append((root.left,q[0][1]-1))
            if(root.right!=None):
                q.append((root.right,q[0][1]+1))
            if (q[0][1] not in d):
                d[q[0][1]]=root.data
            q.pop(0)
        for i in sorted(d):
            print(d[i],end=" ")


    def bottomview(self,root):
        if (root==None):
            return 
        d={}
        q=[(root,0)]
        while q:
            root=q[0][0]
            
            if(root.right!=None):
                q.append((root.right,q[0][1]+1))
            if(root.left!=None):
                q.append((root.left,q[0][1]-1))
            if (q[0][1] not in d):
                d[q[0][1]]=root.data
            q.pop(0)
        for i in sorted(d):
            print(d[i],end=" ")
                
    
            
        
    

tree = Binary_tree()
root = tree.create_node(6)
tree.insert(root, 7)
tree.insert(root, 8)
tree.insert(root, 9)
tree.insert(root, 10)
tree.insert(root, 20)

print("left view")
tree.leftview(root, 0, [])
print("right view")
tree.rightview(root, 0, [])
#y = tree.top(root, 0, {})
#print(y)
#print(y.values())
#print()
tree.topview(root)
tree.bottomview(root)


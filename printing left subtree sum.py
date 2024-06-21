#printing leaf nodes
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class Binary_tree:
    def create_node(self,data):
        return Node(data)
    def insert(self,node,data):
        if node is None:
            return self.create_node(data)
        if data<node.data:
            node.left=self.insert(node.left,data)
        else:
            node.right=self.insert(node.right,data)
        return node
    def find_sumofleftsubtree(self,root):
        if root is None:
            return 0
        s1=root.data
        s2=self.find_sumofleftsubtree(root.left)
        s3=self.find_sumofleftsubtree(root.right)
        return s1+s2+s3
        #return root.data+self.find_sumnodes(root.left)+self.find_sumnodes(root.right)
            
tree=Binary_tree()
root=tree.create_node(10)
#print("root node:",root.data)
tree.insert(root,20)
tree.insert(root,5)
tree.insert(root,2)
tree.insert(root,40)
tree.insert(root,12)
print(tree.find_sumofleftsubtree(root.left))




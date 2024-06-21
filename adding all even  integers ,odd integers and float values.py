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
    def height(self,root):
        if root is None :
            return -1
        return max(self.height(root.left),self.height(root.right))+1

    def balance(self,root):
        return abs(self.height(root.left)-self.height(root.right))<=1        
tree=Binary_tree()
root=tree.create_node(10)
tree.insert(root,20)
tree.insert(root,5)
tree.insert(root,2)
tree.insert(root,40)
tree.insert(root,12)
if(tree.balance(root)):
    print("Balanced")
else:
    print("Not Balanced")

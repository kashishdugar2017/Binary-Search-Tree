class Node:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None
        
class BST:
    def __init__(self):
        self.root = None
        
    def insert(self, value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
        else:
            current = self.root
            while True:
                if current.value > value:
                    if current.left == None:
                        current.left = new_node
                        return new_node
                    else:
                        current = current.left
                else:
                    if current.right == None:
                        current.right = new_node
                        return new_node
                    else:
                        current = current.right
                        
                        
    def inorder(self, node):
        if node is None:
            return       
        self.inorder(node.left)
        print(node.value)
        self.inorder(node.right)
        
    def preorder(self, node):
        if node is None:
            return
        print(node.value)
        self.preorder(node.left)
        self.preorder(node.right)
        
    def postorder(self, node):
        if node is None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.value)


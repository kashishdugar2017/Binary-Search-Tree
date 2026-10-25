class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self,value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
        else:
            current = self.root
            while True:
                if value < current.value:
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

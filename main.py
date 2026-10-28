from bst import * 

tree = BST()

tree.insert(5)
tree.insert(3)
tree.insert(8)
tree.insert(1)


print('Lets test preorder')
tree.preorder(tree.root)
print('Lets test inorder')
tree.inorder(tree.root)
print('Lets test postorder')
tree.postorder(tree.root)

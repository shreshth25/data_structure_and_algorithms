# Class Tree Node
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Creating Tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

root.right.left = TreeNode(6)
root.right.right = TreeNode(7)


#visualization

#               1
#           2      3
#        4     5  6    7


# In Order Traversal
def inorder_traversal(root):
    if not root:
        return
    inorder_traversal(root.left)
    print(root.val, end=" ")
    inorder_traversal(root.right)

# Pre Order Traversal
def preorder_traversal(root):
    if not root:
        return
    print(root.val, end=" ")
    preorder_traversal(root.left)
    preorder_traversal(root.right)


# Post Order Traversal
def postorder_traversal(root):
    if not root:
        return
    postorder_traversal(root.left)
    postorder_traversal(root.right)
    print(root.val, end=" ")





# Execution
print("In order traversal of the tree")
inorder_traversal(root)
print("\nPre order traversal of the tree")
preorder_traversal(root)
print("\nPost order traversal of the tree")
postorder_traversal(root)
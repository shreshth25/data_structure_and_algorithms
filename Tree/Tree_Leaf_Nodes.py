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


# leaf of Nodes
def leaf_nodes(root):
    if not root:
        return
    if root.left == None and root.right == None:
        print(root.val, end = ' ')
    leaf_nodes(root.left)
    leaf_nodes(root.right)

# Execution
print("Leaf nodes of the tree")
leaf_nodes(root)

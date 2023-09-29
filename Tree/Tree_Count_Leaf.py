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


# Leaf of Nodes
def leaf_nodes(root,s):
    if not root:
        return 0
    if root.left == None and root.right == None:
        s.append(1)
    leaf_nodes(root.left, s)
    leaf_nodes(root.right, s)
    return s

# Execution
print("Leaf nodes of the tree")
s = []
print(sum(leaf_nodes(root, s)))
